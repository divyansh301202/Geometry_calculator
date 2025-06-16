import streamlit as st
import requests

API_URL = "https://geometry-calculator-2.onrender.com"

st.set_page_config(page_title="Geometry Calculator", layout="centered")

st.title("📐 Geometry Calculator")
st.markdown("Calculate **area & perimeter** (2D) or **surface area & volume** (3D) for common shapes.")

mode = st.radio("Select Calculation Type:", ["2D Shapes", "3D Shapes"])

st.divider()

if mode == "2D Shapes":
    shape = st.selectbox("Choose a 2D Shape", ["Square", "Rectangle", "Circle", "Triangle"])

    if shape == "Square":
        side = st.number_input("Enter Side Length", min_value=0.0, step=0.1)
        if st.button("Calculate", key="square"):
            res = requests.post(f"{API_URL}/area_perimeter/square", json={"side": side}).json()
            st.success("✅ Results")
            st.metric("Area", f"{res['area']:.2f}")
            st.metric("Perimeter", f"{res['perimeter']:.2f}")

    elif shape == "Rectangle":
        col1, col2 = st.columns(2)
        with col1:
            l = st.number_input("Length", min_value=0.0, step=0.1)
        with col2:
            w = st.number_input("Width", min_value=0.0, step=0.1)

        if st.button("Calculate", key="rectangle"):
            res = requests.post(f"{API_URL}/area_perimeter/rectangle", json={"length": l, "width": w}).json()
            st.success("✅ Results")
            st.metric("Area", f"{res['area']:.2f}")
            st.metric("Perimeter", f"{res['perimeter']:.2f}")

    elif shape == "Circle":
        r = st.number_input("Enter Radius", min_value=0.0, step=0.1)
        if st.button("Calculate", key="circle"):
            res = requests.post(f"{API_URL}/area_perimeter/circle", json={"radius": r}).json()
            st.success("✅ Results")
            st.metric("Area", f"{res['area']:.2f}")
            st.metric("Perimeter (Circumference)", f"{res['perimeter']:.2f}")

    elif shape == "Triangle":
        st.markdown("#### Enter Dimensions:")
        base = st.number_input("Base", min_value=0.0, step=0.1)
        height = st.number_input("Height", min_value=0.0, step=0.1)
        a = st.number_input("Side a", min_value=0.0, step=0.1)
        b = st.number_input("Side b", min_value=0.0, step=0.1)
        c = st.number_input("Side c", min_value=0.0, step=0.1)

        if st.button("Calculate", key="triangle"):
            res = requests.post(f"{API_URL}/area_perimeter/triangle", json={
                "base": base, "height": height, "a": a, "b": b, "c": c
            }).json()
            st.success("✅ Results")
            st.metric("Area", f"{res['area']:.2f}")
            st.metric("Perimeter", f"{res['perimeter']:.2f}")

else:
    shape = st.selectbox("Choose a 3D Shape", ["Cube", "Cuboid", "Sphere", "Cone"])

    if shape == "Cube":
        side = st.number_input("Enter Side Length", min_value=0.0, step=0.1)
        if st.button("Calculate", key="cube"):
            res = requests.post(f"{API_URL}/surface_volume/cube", json={"side": side}).json()
            st.success("✅ Results")
            st.metric("Surface Area", f"{res['surface_area']:.2f}")
            st.metric("Volume", f"{res['volume']:.2f}")

    elif shape == "Cuboid":
        l = st.number_input("Length", min_value=0.0, step=0.1)
        w = st.number_input("Width", min_value=0.0, step=0.1)
        h = st.number_input("Height", min_value=0.0, step=0.1)
        if st.button("Calculate", key="cuboid"):
            res = requests.post(f"{API_URL}/surface_volume/cuboid", json={"length": l, "width": w, "height": h}).json()
            st.success("✅ Results")
            st.metric("Surface Area", f"{res['surface_area']:.2f}")
            st.metric("Volume", f"{res['volume']:.2f}")

    elif shape == "Sphere":
        r = st.number_input("Enter Radius", min_value=0.0, step=0.1)
        if st.button("Calculate", key="sphere"):
            res = requests.post(f"{API_URL}/surface_volume/sphere", json={"radius": r}).json()
            st.success("✅ Results")
            st.metric("Surface Area", f"{res['surface_area']:.2f}")
            st.metric("Volume", f"{res['volume']:.2f}")

    elif shape == "Cone":
        r = st.number_input("Radius", min_value=0.0, step=0.1)
        h = st.number_input("Height", min_value=0.0, step=0.1)
        if st.button("Calculate", key="cone"):
            res = requests.post(f"{API_URL}/surface_volume/cone", json={"radius": r, "height": h}).json()
            st.success("✅ Results")
            st.metric("Surface Area", f"{res['surface_area']:.2f}")
            st.metric("Volume", f"{res['volume']:.2f}")
