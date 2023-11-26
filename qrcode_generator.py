import qrcode

def generate_qr_code(data, file_name):

    # Create QR Code instance 
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    # Add data to the qr code
    qr.add_data(data)
    qr.make(fit = True)

    img = qr.make_image(fill_color = "black", back_color = "white")

    img.save(file_name)

if __name__ == '__main__':
    # Example usage
    data_to_encode = "https://www.example.com"
    output_file = "example_qrcode.png"

    generate_qr_code(data_to_encode, output_file)
    print(f"QR code generated and saved as {output_file}")