# Import các thư viện cần thiết
import argparse
import joblib  # hoặc thư viện tương tự để load model

def run_trained_model(model_file, input_data):
    # Load model từ tệp đã được đào tạo
    model = joblib.load(model_file)

    # Chạy model trên dữ liệu đầu vào
    result = model.predict(input_data)

    # In kết quả hoặc thực hiện các bước xử lý khác dựa trên kết quả

    print("Model prediction result:", result)

if __name__ == "__main__":
    # Sử dụng argparse để lấy đối số dòng lệnh
    parser = argparse.ArgumentParser(description="Run trained model")
    parser.add_argument("model_file", help="Path to the trained model file")
    parser.add_argument("input_data", help="Input data for model prediction")
    args = parser.parse_args()

    # Gọi hàm chạy model với các đối số từ dòng lệnh
    run_trained_model(args.model_file, args.input_data)
