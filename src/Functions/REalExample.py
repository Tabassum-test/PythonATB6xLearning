def validate_response(response_code):
    if response_code == 200:
        print("Request is success")
    else:
        print("Error")

validate_response(400)
validate_response(200)
validate_response(response_code=200)
validate_response(input("Enter your response :"))