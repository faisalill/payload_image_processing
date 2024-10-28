from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
from algorithms.average_box_filter import average_box_filter
from algorithms.bilateral_filter import bilateral_filter
from algorithms.canny_filter import canny_filter
from algorithms.edge_detection import edge_detection
from algorithms.erosion_and_dilation import dilation, erosion
from algorithms.fourier_transform import fourier_transform
from algorithms.gaussian_filter import gaussian_entire_image
from algorithms.histogram_equalization import histogram_equalization
from algorithms.k_means_clustering import k_means_clustering
from algorithms.kalman_filter import kalman_filter
from algorithms.median_filtering import mode_filter, median_filter
from algorithms.image_encoder import image_encoder, image_encoder_pillow
from algorithms.scharr_filter import scharr_filter
from algorithms.types import algorithms
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=['GET'])
def health_check():
    return jsonify({
        "message": "OK"
    })

@app.route('/', methods=['POST'])
def image_test():
    try: 
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            in_memory_file = file.read()
            nparr = np.frombuffer(in_memory_file, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Pillow
            pillow_image = Image.fromarray(img_rgb)
            if img is None:
                return jsonify({'error': 'Unable to decode image'}), 400

            processed_image = None

            print(request.args.get("algoType"))

            match request.args.get("algoType"):
                case algorithms.EdgeDetection:
                    threshold1 = request.args.get("threshold1")
                    threshold2 = request.args.get("threshold2")
                    processed_image = edge_detection(img,int(threshold1), int(threshold2))
                case algorithms.Dilation:
                    kernel1 = request.args.get("kernel1")
                    kernel2 = request.args.get("kernel2")
                    processed_image = dilation(img, int(kernel1), int(kernel2)) 
                case algorithms.Erosion:
                    kernel1 = request.args.get("kernel1")
                    kernel2 = request.args.get("kernel2")
                    processed_image = erosion(img, int(kernel1), int(kernel2)) 
                case algorithms.FourierTransform:
                    processed_image = fourier_transform(img)
                case algorithms.GaussianFilter:
                    processed_image = gaussian_entire_image(img)
                case algorithms.HistogramEqualization:
                    processed_image = histogram_equalization(img)
                case algorithms.KMeansClustering:
                    clusters = request.args.get("clusters")
                    processed_image = k_means_clustering(img, int(clusters))
                case algorithms.MedianFiltering:
                    size = request.args.get("size")
                    match request.args.get("filterType"):
                        case "median":
                            processed_image = median_filter(pillow_image, int(size))
                            encoded_image = image_encoder_pillow(processed_image)
                            return jsonify({'message': 'Image Processed Successfully', 'image': encoded_image}), 200
                        case _:
                            processed_image = mode_filter(pillow_image, int(size))
                            encoded_image = image_encoder_pillow(processed_image)
                            return jsonify({'message': 'Image Processed Successfully', 'image': encoded_image}), 200
                case algorithms.ScharrFilter:
                    processed_image = scharr_filter(img)
                case algorithms.KalmanFilter:
                    processed_image = kalman_filter(img)
                case algorithms.CannyFilter:
                    processed_image = canny_filter(img)
                case algorithms.BilateralFilter:
                    processed_image = bilateral_filter(img)
                case algorithms.AverageBoxFilter:
                    processed_image = average_box_filter(img)
                case _:
                    processed_image = edge_detection(img)

            encoded_image = image_encoder(processed_image)
            return jsonify({'message': 'Image Processed Successfully', 'image': encoded_image}), 200
    except Exception as e:
        print("ERROR: ", e)
        return jsonify({"error:"}), 400

    


if __name__ == "__main__":
    app.run(debug=True)
