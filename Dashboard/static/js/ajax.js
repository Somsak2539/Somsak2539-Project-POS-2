

// ✅ ค้นหา element ที่ใช้แสดงข้อมูลสินค้า
const productContainer = document.getElementById("product-container");
const productContainer1 = document.getElementById("product-container1");
const inputBtn1 = document.querySelector(".add-to-cart-btn");
let ajaxStockAdjustments = []; // เก็บสินค้าที่เพิ่มเข้าไปในตะกร้า
let StockAdjustments = [];
let blogArray = []; // เก็บข้อมูลสินค้าจาก API
const inputBtn3 = document.querySelector(".custom-button4"); // สำหรับปุ่มรับเงิน


if (!productContainer || !productContainer1) {
    console.error(
        "❌ ไม่พบ element productContainer หรือ productContainer1 ใน HTML"
    );
}



// ✅ โหลดข้อมูลสินค้าจาก API
fetch("http://localhost:8080/blog/list/")
    .then((response) => response.json())
    .then((data) => {
        blogArray = data; // กำหนดค่าให้ตัวแปร
        console.log("✅ API Data Loaded:", blogArray);
    })
    .catch((error) => console.error("❌ Error fetching data:", error));








document.addEventListener("click", function (event) {
    if (event.target.classList.contains("add-to-cart-btn")) {
        const productId = event.target.dataset.productId;

        if (blogArray.length === 0) {
            console.warn("⚠️ blogArray ยังไม่ได้โหลดข้อมูลจาก API");
            return;
        }

        const product = blogArray.find((item) => item.id == productId);
        if (!product) {
            console.error("❌ ไม่พบสินค้า ID:", productId);
            return;
        }

        console.log("✅ เพิ่มสินค้า AJAX:", product.name);

        // ✅ ดึงค่าจาก input field
        const inputField = document.getElementById(`quantity-${productId}`);
        if (!inputField) {
            console.error(`❌ ไม่พบ input field id="quantity-${productId}"`);
            return;
        }

        let addedQuantity = parseFloat(inputField.value) || 1;
        if (addedQuantity < 1) {
            console.warn("⚠️ จำนวนสินค้าต้องมากกว่า 0");
            return;
        }

        let totalProfit = product.profitprice * addedQuantity;
        let totalPrice = product.price * addedQuantity;

        // ✅ ค้นหาสินค้าใน ajaxStockAdjustments และอัปเดต
        let existingProduct = ajaxStockAdjustments.find((item) => item.product === product.name);

        if (existingProduct) {
            existingProduct.quantity += addedQuantity; // ✅ รวม quantity เดิม
            existingProduct.totalProfit += totalProfit;
            existingProduct.TotalPrice += totalPrice;
        } else {
            ajaxStockAdjustments.push({
                product: product.name,
                quantity: addedQuantity,
                totalProfit: totalProfit,
                TotalPrice: totalPrice
            });
        }

        console.log("📤 ajaxStockAdjustments ล่าสุด:", ajaxStockAdjustments);
        
        document.dispatchEvent(new CustomEvent("updateStock", { detail: ajaxStockAdjustments }));

        updateCartTable(product, addedQuantity);
        updateTotalAmount();





        // ✅ อัปเดตตารางสินค้า
        updateCartTable(product, addedQuantity);
        updateTotalAmount(); // คำนวณยอดรวมใหม่

        // ✅ อัปเดตภาพสินค้า
        if (productContainer) {
            productContainer.innerHTML = product.image
                ? `<div class="img2"><img src="${product.image}" alt="${product.name}" /></div>`
                : `<div class="img2">ไม่มีรูปภาพ</div>`;
        }

        if (productContainer1) {
            productContainer1.innerHTML = `
                  <h6>
                      - สินค้าใน stock: ${product.stock} pcs <br />
                      - ชื่อสินค้า: ${product.name} <br />
                      - ราคา: ${product.price} บาท <br />
                  </h6>`;
        }


      



        // ✅ รีเซ็ตค่าแสดงผล
        const calculatorDisplay = document.getElementById("calculatorDisplay");
        if (calculatorDisplay) {
            calculatorDisplay.textContent = "0";
        } else {
            console.error("❌ ไม่พบ element calculatorDisplay ใน HTML");
        }

        selectedItem = "";
    }
});









// ✅ ฟังก์ชันเพิ่มสินค้าเข้าไปในตาราง
function updateCartTable(product, quantity) {
    console.log("🔍 ตรวจสอบค่า product:", product);

    if (!product || !product.name) {
        console.error("❌ Error: ไม่พบข้อมูลสินค้า หรือ product.name เป็น undefined!");
        return;
    }

    const cartBody = document.getElementById("itemTableBody");

    // ✅ ค้นหาข้อมูลสินค้าจาก ajaxStockAdjustments แทนการดึงจาก <td>
    let updatedProduct = ajaxStockAdjustments.find(item => item.product === product.name);

    if (!updatedProduct) {
        console.warn(`⚠️ ไม่พบสินค้า ${product.name} ใน ajaxStockAdjustments`);
        return;
    }

    let existingRow = document.querySelector(`#itemTableBody tr[data-barcode="${product.barcode}"]`);

    if (existingRow) {
        console.log("🟢 อัปเดตจำนวนสินค้าในตาราง:", product.name);

        let quantityCell = existingRow.querySelector(".cart-quantity");
        let totalCell = existingRow.querySelector(".cart-total");

        // ✅ ใช้ค่าล่าสุดจาก ajaxStockAdjustments
        let newQuantity = updatedProduct.quantity;
        let newTotalPrice = updatedProduct.TotalPrice;

        quantityCell.innerText = newQuantity.toFixed(2);
        totalCell.innerText = newTotalPrice.toLocaleString(undefined, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
        }) + " บาท";

    } else {
        console.log("🆕 เพิ่มสินค้าใหม่ลงในตาราง:", product.name);
        let row = document.createElement("tr");
        row.setAttribute("data-barcode", product.barcode); // ใช้ barcode เป็น identifier

        row.innerHTML = `
            <td class="1border p-2">${product.id}</td>
            <td class="1border p-2">${product.barcode}</td>
            <td class="1border p-2">${product.name}</td>
            <td class="1border p-2">Kg/pcs</td>
            <td class="1border p-2 cart-quantity">${updatedProduct.quantity.toFixed(2)}</td>
            <td class="1border p-2 cart-total">${updatedProduct.TotalPrice.toLocaleString(undefined, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
        })} บาท</td>
            <td class="1border p-2">${product.stock}</td>
            <td class="1border p-2">
                <button type="button" class="btn btn-danger remove-item">ลบข้อมูล</button>
            </td>
        `;
        cartBody.appendChild(row);
    }

    addRemoveEvent(); // ✅ อัปเดต Event Listener
}









// ✅ ฟังก์ชันคำนวณยอดรวม
function updateTotalAmount() {
    let totalAmount = ajaxStockAdjustments.reduce(
        (sum, item) => sum + item.TotalPrice,
        0
    );
    document.getElementById(
        "totalAmount"
    ).innerText = `${totalAmount.toLocaleString(undefined, {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    })} บาท`;
}

function addRemoveEvent() {
    document.querySelectorAll(".remove-item").forEach((button) => {
        button.addEventListener("click", function () {
            let row = this.closest("tr");
            let productName = row.querySelector("td:nth-child(3)").innerText;

            // ลบแถวออกจากตาราง
            row.remove();

            // ลบข้อมูลออกจาก ajaxStockAdjustments
            console.log("ก่อนลบ:", ajaxStockAdjustments);
            ajaxStockAdjustments = ajaxStockAdjustments.filter(
                (item) => item.product !== productName
            );
            console.log("หลังลบ:", ajaxStockAdjustments);




            if (existingProduct) {
                console.log("🔄 พบสินค้านี้อยู่แล้ว:", existingProduct);
                console.log("📌 ค่าที่ถูกเพิ่ม:", addedQuantity);

                existingProduct.quantity += addedQuantity;
                existingProduct.totalProfit += totalProfit;
                existingProduct.TotalPrice += totalPrice;
            } else {
                console.log("🆕 เพิ่มสินค้าใหม่:", product.name);

                ajaxStockAdjustments.push({
                    product: product.name,
                    quantity: addedQuantity,
                    totalProfit: totalProfit,
                    TotalPrice: totalPrice
                });
            }

            // ✅ เช็คค่าทั้งหมดก่อนส่งไป script.js
            console.log("📦 ajaxStockAdjustments (หลังเพิ่มสินค้าใน ajax.js):", ajaxStockAdjustments);

            // ✅ ส่ง Event ไปให้ script.js
            document.dispatchEvent(new CustomEvent("updateStock", { detail: ajaxStockAdjustments }));
            console.log("📤 ส่ง Event updateStock พร้อมข้อมูลไป script.js:", ajaxStockAdjustments);

            // ------------------------------อัปเดต LocalStorage ส่งข้ามไฟค์---------------------------------
            localStorage.setItem("ajaxStockAdjustments", JSON.stringify(ajaxStockAdjustments));
            // ส่ง Event ไปให้ไฟล์อื่น (ถ้าจำเป็น)
            document.dispatchEvent(new CustomEvent("updateStock", { detail: ajaxStockAdjustments }));

            // คำนวณยอดรวมใหม่
            updateTotalAmount();
        });
    });
}

// ------------------------------------------------------------------------สำหรับการแอด update Stock-------------------------------------



//********************************************************************* */

// ✅ โหลดข้อมูลสินค้าจาก API
fetch("http://localhost:8080/blog/list/")
    .then((response) => response.json())
    .then((data) => {
        blogArray = data;
        console.log("✅ API Data Loaded:", blogArray);
    })
    .catch((error) => console.error("❌ Error fetching data:", error));

// ✅ ฟังก์ชันดึงค่า CSRF Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}







