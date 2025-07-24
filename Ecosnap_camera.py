import streamlit as st
from datetime import datetime
from PIL import Image
import io
from geopy.geocoders import Nominatim

# Function to get location from user input
def get_location():
    geolocator = Nominatim(user_agent="eco_snap")
    location_input = st.text_input("Enter your location (e.g., City, Country):")
    if location_input:
        location = geolocator.geocode(location_input)
        if location:
            return f"{location.latitude}, {location.longitude}"
        else:
            st.warning("Location not found. Please enter a valid location.")
    return None

# EcoSnap Camera Feature
def eco_snap_camera():
    st.title("EcoSnap Camera")
    st.markdown("""
    ### Capture Your Eco-Friendly Action
    Please upload an image of your eco-friendly action (e.g., using public transport, carrying reusable items, cycling, composting, or participating in tree planting drives).
    """)

    # File uploader simulating camera capture in browser
    uploaded_file = st.file_uploader("Upload an image of your eco-friendly action", type=['png', 'jpg', 'jpeg'])

    # Location input (simulating optional metadata)
    location = get_location()

    # Display timestamp automatically
    timestamp = datetime.now()
    st.write(f"Timestamp (capture time): {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Simulate filters or prompts using a selectbox - user can choose a filter to preview
        filter_option = st.selectbox("Choose a filter overlay to preview (simulated)", ["None", "Green Tint", "Black & White", "Sepia"])

        # Simple filter simulation
        if filter_option != "None":
            img = image.convert("RGB")
            if filter_option == "Green Tint":
                r, g, b = img.split()
                g = g.point(lambda i: i * 1.5)
                filtered = Image.merge('RGB', (r, g, b))
                st.image(filtered, caption=f"Filter applied: {filter_option}", use_column_width=True)
            elif filter_option == "Black & White":
                filtered = img.convert("L")
                st.image(filtered, caption=f"Filter applied: {filter_option}", use_column_width=True)
            elif filter_option == "Sepia":
                sepia_img = img.convert("RGB")
                width, height = sepia_img.size
                pixels = sepia_img.load()  # create the pixel map

                for py in range(height):
                    for px in range(width):
                        r, g, b = sepia_img.getpixel((px, py))

                        tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                        tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                        tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                        tr = min(255, tr)
                        tg = min(255, tg)
                        tb = min(255, tb)

                        pixels[px, py] = (tr, tg, tb)
                st.image(sepia_img, caption=f"Filter applied: {filter_option}", use_column_width=True)

        # Simulate submit button for upload
        if st.button("Submit Eco-Friendly Action"):
            # Here backend upload and processing would happen
            st.success("Image and metadata submitted successfully!")
            st.json({
                "filename": uploaded_file.name,
                "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                "location": location if location else "Not provided"
            })
    else:
        st.info("Please upload an image to continue.")

# Run the EcoSnap Camera feature
if __name__ == "__main__":
    eco_snap_camera()
