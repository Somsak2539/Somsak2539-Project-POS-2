document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ AJAX JavaScript Loaded!");
    
    document.getElementById("load-products").addEventListener("click", function () {
        fetch("/get-products/")
            .then(response => response.json())
            .then(data => {
                console.log("📌 ดึงข้อมูลจาก Backend:", data);
                updateProductTable(data);
            })
            .catch(error => console.error("❌ เกิดข้อผิดพลาด:", error));
    });
});

// ✅ ฟังก์ชันเพิ่มสินค้าไปยังตาราง
function updateProductTable(products) {
    const cartBody = document.getElementById("cart-body");
    cartBody.innerHTML = ""; // เคลียร์ข้อมูลเดิม

    products.forEach(product => {
        let row = document.createElement("tr");
        row.innerHTML = `
            <td class="border p-2">${product.id}</td>
            <td class="border p-2">${product.name}</td>
            <td class="border p-2">${product.price}</td>
            <td class="border p-2">${product.stock}</td>
        `;
        cartBody.appendChild(row);
    });
}
