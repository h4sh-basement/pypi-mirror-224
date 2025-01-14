from enum import Enum
from typing import Dict, List, Tuple

import numpy as np

from visiongraph.data.RepositoryAsset import RepositoryAsset
from visiongraph.estimator.spatial.face.OpenVinoFaceDetector import OpenVinoFaceDetector


class AdasFaceConfig(Enum):
    MobileNet_672x384_FP32 = RepositoryAsset.openVino("face-detection-adas-0001")


class AdasFaceDetector(OpenVinoFaceDetector):
    def _get_results(self, outputs: Dict[str, np.ndarray]) -> List[Tuple[float, float, float, float, float]]:
        output = outputs[self.engine.output_names[0]]

        results = []

        for obj in output[0][0]:
            score = float(obj[2])
            if score > self.min_score:
                xmin = float(obj[3])
                ymin = float(obj[4])
                xmax = float(obj[5])
                ymax = float(obj[6])

                results.append((score, xmin, ymin, xmax, ymax))

        return results

    @staticmethod
    def create(config: AdasFaceConfig = AdasFaceConfig.MobileNet_672x384_FP32) -> "AdasFaceDetector":
        model, weights = config.value
        return AdasFaceDetector(model, weights)
