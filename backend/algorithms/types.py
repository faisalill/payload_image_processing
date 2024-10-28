from collections import namedtuple

AlgorithmAccess = namedtuple('AlgorithmAccess', [
    'EdgeDetection', 'Erosion', 'Dilation', 'FourierTransform',
    'GaussianFilter', 'HistogramEqualization', 'KMeansClustering',
    'MedianFiltering', 'WaveletTransformFilter', 'ScharrFilter',
    'KalmanFilter', "CannyFilter","BilateralFilter","AverageBoxFilter"
])

algorithms = AlgorithmAccess(
    EdgeDetection="edge_detection",
    Erosion="erosion",
    Dilation="dilation",
    FourierTransform="fourier_transform",
    GaussianFilter="gaussian_filter",
    HistogramEqualization="histogram_equalization",
    KMeansClustering="k_means_clustering",
    MedianFiltering="median_filtering",
    WaveletTransformFilter="wavelet_transform_filter",
    ScharrFilter="scharr_filter",
    KalmanFilter="kalman_filter",
    CannyFilter="canny_filter",
    BilateralFilter="bilateral_filter",
    AverageBoxFilter="average_box_filter"
)

