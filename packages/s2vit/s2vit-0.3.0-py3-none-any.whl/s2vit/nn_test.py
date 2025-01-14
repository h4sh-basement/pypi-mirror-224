import torch

from .nn import WindowMHSA


def test_BlockMHSA_forward():
    """Confirm BlockMHSA forward pass works as expected."""
    x = torch.randn(1, 8, 16, 16)
    block = WindowMHSA(dim=8, heads=2, dim_head=4, window_size=4, drop_rate=0.0, bias=False)
    out = block(x)
    assert out.shape == x.shape


def test_BlockMHSA_shared_kv_forward():
    """Confirm BlockMHSA forward pass works as expected."""
    x = torch.randn(1, 8, 16, 16)
    block = WindowMHSA(dim=8, heads=2, dim_head=4, window_size=4, shared_kv=True, drop_rate=0.0, bias=False)
    out = block(x)
    assert out.shape == x.shape
