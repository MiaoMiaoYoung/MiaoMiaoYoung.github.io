---
title: "MAE is all you need"
date: 2022-11-19T15:01:38+08:00
draft: false
categories:
    - 学习
    - work
    - paper
    - mae

libraries:
- katex

enableTocContent: true
---

## Mask Autoencoder (Code)

### Encoder

- img_size: 224

- patch_size: 16

```python
def forward_encoder(self, x, mask_ratio):
    # embed patches
    x = self.patch_embed(x)

    # add pos embed w/o cls token
    x = x + self.pos_embed[:, 1:, :]

    # masking: length -> length * mask_ratio
    x, mask, ids_restore = self.random_masking(x, mask_ratio)

    # append cls token
    cls_token = self.cls_token + self.pos_embed[:, :1, :]
    cls_tokens = cls_token.expand(x.shape[0], -1, -1)
    x = torch.cat((cls_tokens, x), dim=1)

    # apply Transformer blocks
    for blk in self.blocks:
        x = blk(x)
    x = self.norm(x)

    return x, mask, ids_restore
```


- PatchEmbed

    ```python
    from timm.models.vision_transformer import PatchEmbed
    def PatchEmbed(img_size, patch_size, in_chans, embed_dim)
    ```

    - 将大小为 [ batch_size, 3, img_size, img_size] 的图片tensor切成 [batch_size, patch_num, path_embed_length] 的{1, 196, 768} Patch Embed向量

    - Patch的个数： patch_num = (img_size / patch_size ) {14} ** 2 = 196

    - Patch Embeding 长度： path_embed_length = patch_size {16} ** 2 *3 = 768

- self.pos_embed

    sin-cos 位置编码 [ 1, patch_num+1, path_embed_length]

    ```python
    pos_embed = get_2d_sincos_pos_embed(
        self.pos_embed.shape[-1], 
        int(self.patch_embed.num_patches ** .5),
        cls_token=True)
    self.pos_embed.data.copy_(torch.from_numpy(pos_embed).float().unsqueeze(0))
    ```