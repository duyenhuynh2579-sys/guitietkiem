import streamlit as st

# Tiêu đề ứng dụng
st.title("Tính tiền khách hàng nhận được theo lãi đơn")

# Nhập dữ liệu
c = st.number_input("Nhập số tiền gửi (triệu đồng)", min_value=0.0, value=160.0)
i = st.number_input("Nhập lãi suất năm (%)", min_value=0.0, value=4.0) / 100
n = st.number_input("Nhập số tháng gửi", min_value=1, value=3)

# Nút tính toán
if st.button("Tính tiền"):
    a = c * (i * n / 12 + 1)
    st.success(f"Số tiền khách hàng nhận được theo lãi đơn: {a:,.2f} triệu đồng")
