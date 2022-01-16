from typing import List, Tuple

import matplotlib.pyplot as plt
from math import sqrt
from torch import Tensor


def visualize_snapshots_grid_progress_2d(snapshots: List[Tuple[int, Tensor, Tensor]]):
    batch_size = snapshots[0][1].shape[0]
    subplot_size = sqrt(batch_size)
    for snapshot_epoch, snapshot in snapshots:
        print(f"\n\n Results At Epoch {snapshot_epoch} \n\n")
        plt.figure(figsize=(6, 6))
        for i in range(batch_size):
            plt.subplot(subplot_size, subplot_size, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.axis('off')
            plt.grid(False)
            plt.imshow(snapshot[i][0][:, :].detach().cpu(), cmap=plt.cm.gray_r)
        plt.show()


def visualize_snapshots(snapshots: List[Tuple[int, Tensor, Tensor]]):
    for snapshot_epoch, snapshot_A, snapshot_B in snapshots:
        print(f"\n\n Results At Epoch {snapshot_epoch} \n\n")
        plt.figure(figsize=(6, 6))
        for i in range(2):
            plt.subplot(1, 2, 1)
            plt.xticks([])
            plt.yticks([])
            plt.axis("off")
            plt.grid(False)
            plt.imshow(snapshot_A[0].swapaxes(0, 1).swapaxes(1, 2).cpu())
            plt.subplot(1, 2, 2)
            plt.xticks([])
            plt.yticks([])
            plt.axis("off")
            plt.grid(False)
            plt.imshow(
                snapshot_B[0].swapaxes(0, 1).swapaxes(1, 2).cpu()
            )
        plt.show()
