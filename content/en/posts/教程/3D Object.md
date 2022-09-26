---
title: "3D Objects"
date: 2022-07-07T11:16:18+08:00
draft: false
categories:
    - 教程
tags:
    - python
    - code    
---

在这里放一只[兔兔](https://miaomiaoyoung.github.io/en/posts/%E6%95%99%E7%A8%8B/bunny.obj)

路过的朋友可以摸摸她: (这TM是兔子？)

```
          /＞　  フ
          |   _　_|
　 　　　／` ミ＿꒳ノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ
```

## 创建一个Mesh

不管是下面哪种方法，都要注意在生成一个三角面片时，三个点的先后顺序

E.g. [p0, p1, p2] 还是 [p0, p2, p1]

这个顺序决定了这个面片的法向朝向，朝里/朝外，下面是numpt-stl中给出的法向计算方式：

```python
import numpy as np
normals = np.cross(p1 - p0, p2 - p0)
```



### PyMeshlab

[Import Mesh From Arrays](https://github.com/cnr-isti-vclab/PyMeshLab/blob/main/pymeshlab/tests/example_import_mesh_from_arrays.py)


```python
import pymeshlab
import numpy


def example_import_mesh_from_arrays():
    # lines needed to run this specific example
    print('\n')
    from . import samples_common
    output_path = samples_common.test_output_path()

    # create a numpy 8x3 array of vertices
    # columns are the coordinates (x, y, z)
    # every row represents a vertex
    verts = numpy.array([
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [-0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5]])

    # create a numpy 12x3 array of faces
    # every row represents a face (triangle in this case)
    # for every triangle, the index of the vertex
    # in the vertex array
    faces = numpy.array([
        [2, 1, 0],
        [1, 2, 3],
        [4, 2, 0],
        [2, 4, 6],
        [1, 4, 0],
        [4, 1, 5],
        [6, 5, 7],
        [5, 6, 4],
        [3, 6, 7],
        [6, 3, 2],
        [5, 3, 7],
        [3, 5, 1]])

    # create a new Mesh with the two arrays
    m = pymeshlab.Mesh(verts, faces)

    assert m.vertex_number() == 8
    assert m.face_number() == 12

    # create a new MeshSet
    ms = pymeshlab.MeshSet()

    # add the mesh to the MeshSet
    ms.add_mesh(m, "cube_mesh")

    # save the current mesh
    ms.save_current_mesh(output_path + "saved_cube_from_array.ply")
```

如果是逐步创建的，比如管状结构，一层一层进行构建mesh然后拼接的，可以使用下面的进行合并

```python
import pymeshlab as ml
ms = ml.MeshSet()
for idx in range(1, len(vesselrad)):
    verts = ...
    faces = ...
    ms.add_mesh(ml.Mesh(verts, faces))
ms.apply_filter('generate_by_merging_visible_meshes')

mesh = ms.current_mesh()
return mesh.vertex_matrix(), mesh.face_matrix()
```

这里如果直接返回mesh不知道为啥返回不成功，所以就返回点、面的array，然后在上一级使用pymeshlab.Mesh(verts, faces)再重构出来

### Numpy-STL

> https://numpy-stl.readthedocs.io/en/latest/usage.html#creating-mesh-objects-from-a-list-of-vertices-and-faces

```python
from stl import mesh
import numpy
import stl

data = numpy.zeros(2, dtype=mesh.Mesh.dtype)
data['vectors'][0] = numpy.array([[-1, -1, -1],
                                  [+1, -1, -1],
                                  [+1, +1, -1]])
data['vectors'][1] = numpy.array([[-1, +1, -1],
                                  [-1, -1, +1],
                                  [+1, -1, +1]])

mesh = mesh.Mesh(data)
mesh.save('./test.stl', mode=stl.Mode.ASCII)
```

多个mesh进行拼接：

```python
def combined_stl(meshes, save_path="./combined.stl"):
    combined = mesh.Mesh(np.concatenate([m.data for m in meshes])).is_closed()


    # print(combined.is_closed())
    combined.save(save_path, mode=stl.Mode.ASCII)
```



### PyVista

> https://docs.pyvista.org/examples/00-load/create-poly.html


需要注意，Pyvista和其他略微不同，Pyvista的face需要指定是几个点构成一个面，可能出现由4个点构成的一个面，而其他库大都以三角面片为准

```python
# mesh points
vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, -1]])

# mesh faces
faces = np.hstack(
    [
        [4, 0, 1, 2, 3],  # square
        [3, 0, 1, 4],  # triangle
        [3, 1, 2, 4],  # triangle
    ]
)

surf = pv.PolyData(vertices, faces)

# plot each face with a different color
surf.plot(
    scalars=np.arange(3),
    cpos=[-1, 1, 0.5],
    show_scalar_bar=False,
    show_edges=True,
    line_width=5,
)
```


### Trimesh


## 合并 Mesh

这里的合并不是Merge，将两个mesh简单放到同一个文件里的意思，而是对两个mesh进行操作，合并相同的区域，一般用到的操作是bool union，相对的，还有intersection, xor等操作。但是这些操作的前提都是两个mesh师close的，也就是水密的(watertight)

### Close or not Close

> Close or not Close, it's a question
> 
> Close = Watertight

numpy-stl中给出判断closed的条件，即所有面的法向量之和为0：

```python
from stl import mesh
mesh.Mesh().is_closed()

if numpy.isclose(self.normals.sum(axis=0), 0, atol=1e-4).all():
    return True
```

所以在创建mesh的过程中要十分注意三角面片中三个点的顺序

### pymeshlab

```python
import pymeshlab as ml

ms = ml.MeshSet()
num = 0
for vesselrad in self.vesselrad:
    verts, faces = ...
    ms.add_mesh(ml.Mesh(verts, faces))
    num += 1

current_id = 0
for idx in range(1, num):
    ms.apply_filter('generate_boolean_union', first_mesh=current_id, second_mesh=idx)
    current_id = ms.current_mesh_id()
ms.current_mesh()
```

### pyvista

> https://docs.pyvista.org/examples/index.html
>
> https://docs.pyvista.org/examples/01-filter/boolean-operations.html

```python
import pyvista as pv

sphere_a = pv.Sphere()
sphere_b = pv.Sphere(center=(0.5, 0, 0))

result = sphere_a.boolean_union(sphere_b)
pl = pv.Plotter()
_ = pl.add_mesh(sphere_a, color='r', style='wireframe', line_width=3)
_ = pl.add_mesh(sphere_b, color='b', style='wireframe', line_width=3)
_ = pl.add_mesh(result, color='tan')
pl.camera_position = 'xz'
pl.show()
```

但是不知道为啥，这个库demo可以跑，但是用在我项目里就会段错误segment fault，不过例子还是很好看的


## Mesh IO

### pymeshlab

```python
import pymeshlab
ms = pymeshlab.MeshSet()
ms.load_new_mesh('airplane.obj')
ms.generate_convex_hull()
ms.save_current_mesh('convex_hull.ply')
```

### PyVista

```python
import pyvista

mesh = pv.read(filename)
cpos = mesh.plot()

sphere = pyvista.Sphere()
sphere.save('my_mesh.stl')
```
