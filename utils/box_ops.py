import torch


def iou_score(bboxes_a, bboxes_b):
    """
        Input:\n
        bboxes_a : [N, 4] = [x1, y1, x2, y2] \n
        bboxes_b : [N, 4] = [x1, y1, x2, y2] \n

        Output:\n
        iou : [N,] \n
    """
    tl = torch.max(bboxes_a[:, :2], bboxes_b[:, :2])
    br = torch.min(bboxes_a[:, 2:], bboxes_b[:, 2:])
    area_a = torch.prod(bboxes_a[:, 2:] - bboxes_a[:, :2], 1)
    area_b = torch.prod(bboxes_b[:, 2:] - bboxes_b[:, :2], 1)

    en = (tl < br).type(tl.type()).prod(dim=1)
    area_i = torch.prod(br - tl, 1) * en  # * ((tl < br).all())
    iou = area_i / (area_a + area_b - area_i + 1e-14)

    return iou


def giou_score(bboxes_a, bboxes_b):
    """
        bbox_1 : [N, 4] = [x1, y1, x2, y2]
        bbox_2 : [N, 4] = [x1, y1, x2, y2]
    """
    # iou
    tl = torch.max(bboxes_a[:, :2], bboxes_b[:, :2])
    br = torch.min(bboxes_a[:, 2:], bboxes_b[:, 2:])
    area_a = torch.prod(bboxes_a[:, 2:] - bboxes_a[:, :2], 1)
    area_b = torch.prod(bboxes_b[:, 2:] - bboxes_b[:, :2], 1)

    en = (tl < br).type(tl.type()).prod(dim=1)
    area_i = torch.prod(br - tl, 1) * en  # * ((tl < br).all())
    iou = (area_i / (area_a + area_b - area_i + 1e-14)).clamp(0)
    
    # giou
    tl = torch.min(bboxes_a[:, :2], bboxes_b[:, :2])
    br = torch.max(bboxes_a[:, 2:], bboxes_b[:, 2:])
    en = (tl < br).type(tl.type()).prod(dim=1)
    area_c = torch.prod(br - tl, 1) * en  # * ((tl < br).all())

    giou = (iou - (area_c - area_i) / (area_c + 1e-14))

    return giou


if __name__ == '__main__':
    box1 = torch.tensor([[10, 10, 20, 20]])
    box2 = torch.tensor([[15, 15, 25, 25]])
    iou = iou_score(box1, box2)
    print(iou)
    giou = giou_score(box1, box2)
    print(giou)
