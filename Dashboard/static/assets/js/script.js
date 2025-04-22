document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ JavaScript Loaded in Dashboard!");
    
    const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");

    addToCartButtons.forEach(button => {
        console.log("📌 พบปุ่มเพิ่มสินค้า:", button);
        button.addEventListener("click", function () {
            const productId = this.dataset.productId;
            const quantityField = document.querySelector(`#quantity-${productId}`);
            const quantity = quantityField ? parseInt(quantityField.value, 10) : 1;

            const productNameElement = document.querySelector(`[data-product-name="${productId}"]`);
            const productPriceElement = document.querySelector(`[data-product-price="${productId}"]`);

            if (!productNameElement || !productPriceElement) {
                console.error("❌ ไม่สามารถดึงข้อมูลสินค้าได้");
                return;
            }

            const productName = productNameElement.innerText;
            const productPrice = parseFloat(productPriceElement.innerText);

            console.log("🟢 กำลังเพิ่มสินค้า:", { productId, productName, productPrice, quantity });

            // ✅ อัปเดตตาราง (ไม่ต้องใช้ AJAX)
            updateCartTable(productId, productName, productPrice, quantity);
        });
    });
});

// ✅ ฟังก์ชันอัปเดตตาราง
function updateCartTable(productId, name, price, quantity) {
    console.log("🔄 อัปเดตตาราง -", productId, name, price, quantity);

    const cartBody = document.getElementById("cart-body");
    let existingRow = document.querySelector(`#cart-body tr[data-product-id="${productId}"]`);

    if (existingRow) {
        console.log("🟢 อัปเดตจำนวนสินค้าในตาราง");
        let quantityCell = existingRow.querySelector(".cart-quantity");
        let totalCell = existingRow.querySelector(".cart-total");

        let newQuantity = parseInt(quantityCell.innerText, 10) + quantity;
        quantityCell.innerText = newQuantity;
        totalCell.innerText = (newQuantity * price).toFixed(2);
    } else {
        console.log("🆕 เพิ่มสินค้าใหม่ลงในตาราง");
        let row = document.createElement("tr");
        row.setAttribute("data-product-id", productId);
        row.innerHTML = `
            <td class="border p-2">${productId}</td>
            <td class="border p-2">${name}</td>
            <td class="border p-2">${price.toFixed(2)}</td>
            <td class="border p-2 cart-quantity">${quantity}</td>
            <td class="border p-2 cart-total">${(price * quantity).toFixed(2)}</td>
            <td class="border p-2">
                <button class="remove-item bg-red-500 text-white p-1 rounded">ลบ</button>
            </td>
        `;
        cartBody.appendChild(row);
    }

    addRemoveEvent();
}

// ✅ ฟังก์ชันลบสินค้าออกจากตาราง
function addRemoveEvent() {
    document.querySelectorAll(".remove-item").forEach(button => {
        button.addEventListener("click", function () {
            this.closest("tr").remove();
        });
    });
}
