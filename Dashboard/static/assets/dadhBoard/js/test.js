

// ------------------------------------------------------------------------------การทดสอบ Api------------------------------------------------
const apiUrl = "http://127.0.0.1:8080/blog/list/";






fetch(apiUrl)
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    console.log("API Data:", data); // ตรวจสอบข้อมูลที่ดึงมา
    const blogArray = Array.from(data); // แปลงข้อมูล JSON เป็น Array
    console.log("Converted Array:", blogArray);

    // ตัวอย่างการดึงข้อมูล id 1 และ id 2
    const firstBlog1 = blogArray.find((blog) => blog.id === 1); // หมูกะทะ
    const firstBlog2 = blogArray.find((blog) => blog.id === 2); // คอหมูย่าง
    const firstBlog3 = blogArray.find((blog) => blog.id === 3); // ไส้อ่อน
    const firstBlog4 = blogArray.find((blog) => blog.id === 4); // ใส้ใหญ่
    const firstBlog5 = blogArray.find((blog) => blog.id === 5); // ซี่โคร่งหมู
    const firstBlog6 = blogArray.find((blog) => blog.id === 6); // ไหล่หมู
    const firstBlog7 = blogArray.find((blog) => blog.id === 7); // สันนอก
    const firstBlog8 = blogArray.find((blog) => blog.id === 8); // สามชั้น
    const firstBlog9 = blogArray.find((blog) => blog.id === 9); // กรดูกหมูชูป
    const firstBlog10 = blogArray.find((blog) => blog.id === 10); // หมูบด
    const firstBlog11 = blogArray.find((blog) => blog.id === 11); // สันคอ
    const firstBlog12 = blogArray.find((blog) => blog.id === 12); // ยังไม่ระบุ

    const firstBlog13 = blogArray.find((blog) => blog.name);


    //----------------------------------------------การเพื่มรายการสำหรับการยิงบาร์โค้ด------------------------------- 







    //-------------------------------------------------การเพิ่มรายกานสำหรับการยิงบาร์โค้ด----------------------------

    if (firstBlog1) {
      console.log("First Blog (ID 1):", firstBlog1); // หมูกะทะ
      console.log("Name:", firstBlog1.name);
      console.log("Price:", firstBlog1.price);
      console.log("id:", firstBlog1.id);
      console.log("id:", firstBlog1.stock);
      console.log("barcode", firstBlog1.barcode)
    } else {
      console.log("Blog with ID 1 not found.");
    }

    if (firstBlog2) {
      console.log("Second Blog (ID 2):", firstBlog2); // ขอหมูย่าง
      console.log("Name:", firstBlog2.name);
      console.log("Price:", firstBlog2.price);
      console.log("Price:", firstBlog2.stock);
    } else {
      console.log("Blog with ID 2 not found.");
    }


    if (firstBlog3) {
      console.log("Second Blog (ID 3):", firstBlog3); // ไส้อ้อน
      console.log("Name:", firstBlog3.name);
      console.log("Price:", firstBlog3.price);
      console.log("Price:", firstBlog3.stock);
    } else {
      console.log("Blog with ID 3 not found.");
    }



    if (firstBlog4) {
      console.log("Second Blog (ID 4):", firstBlog4); // ไส้อ่อน
      console.log("Name:", firstBlog4.name);
      console.log("Price:", firstBlog4.price);
      console.log("Price:", firstBlog4.stock);
    } else {
      console.log("Blog with ID 4 not found.");
    }



    if (firstBlog5) {
      console.log("Second Blog (ID 5):", firstBlog5); // ไส้ใหญ่
      console.log("Name:", firstBlog5.name);
      console.log("Price:", firstBlog5.price);
      console.log("Price:", firstBlog5.stock);
    } else {
      console.log("Blog with ID 5 not found.");
    }



    if (firstBlog6) {
      console.log("Second Blog (ID 6):", firstBlog6); // ซี่โครงหมู
      console.log("Name:", firstBlog6.name);
      console.log("Price:", firstBlog6.price);
      console.log("Price:", firstBlog6.stock);
    } else {
      console.log("Blog with ID 6 not found.");
    }




    if (firstBlog7) {
      console.log("Second Blog (ID 2):", firstBlog7); // ไหล่หมู่
      console.log("Name:", firstBlog7.name);
      console.log("Price:", firstBlog7.price);
      console.log("Price:", firstBlog7.stock);
    } else {
      console.log("Blog with ID 7 not found.");
    }



    if (firstBlog8) {
      console.log("Second Blog (ID 8):", firstBlog8); // สันนอก
      console.log("Name:", firstBlog8.name);
      console.log("Price:", firstBlog8.price);
      console.log("Price:", firstBlog8.stock);
    } else {
      console.log("Blog with ID 8 not found.");
    }



    if (firstBlog9) {
      console.log("Second Blog (ID 9):", firstBlog9); // สามชั้น
      console.log("Name:", firstBlog9.name);
      console.log("Price:", firstBlog9.price);
      console.log("Price:", firstBlog9.stock);
    } else {
      console.log("Blog with ID 9 not found.");
    }



    if (firstBlog10) {
      console.log("Second Blog (ID 10):", firstBlog10); // กระดูกซุป
      console.log("Name:", firstBlog10.name);
      console.log("Price:", firstBlog10.price);
      console.log("Price:", firstBlog10.stock);
    } else {
      console.log("Blog with ID 10 not found.");
    }







    // ฟังก์ชันสำหรับแสดงวันที่และเวลา
    function showDateTime() {
      const today = new Date();

      // ดึงข้อมูลวันที่
      const day = today.getDate();
      const month = today.getMonth() + 1; // เดือนเริ่มที่ 0 ต้องบวก 1
      const year = today.getFullYear();

      // ดึงข้อมูลเวลา
      const hours = today.getHours();
      const minutes = today.getMinutes().toString().padStart(2, "0"); // เติม 0 ข้างหน้า ถ้าน้อยกว่า 10
      const seconds = today.getSeconds().toString().padStart(2, "0"); // เติม 0 ข้างหน้า ถ้าน้อยกว่า 10

      // จัดรูปแบบวันที่และเวลาเป็น DD/MM/YYYY HH:MM:SS
      const formattedDateTime = `${day}/${month}/${year} `;
      const Time = `${hours}:${minutes}:${seconds}`;
      // แสดงผลใน HTML
      document.getElementById("current-datetime").innerText = formattedDateTime;
      document.getElementById("time").innerText = Time;
    }

    // เรียกฟังก์ชันครั้งแรก
    showDateTime();

    // อัปเดตวันที่และเวลาทุก ๆ 1 วินาที
    setInterval(showDateTime, 1000);

    //เรียกใช้ฝั่งชั่นสำหรับปุ่มกด



    const calculatorDisplay = document.querySelector(".result-box"); // ตัวแสดงผลในตาราง

    const productContainer = document.getElementById("product-container"); //-------------ประกาศสำหรับการเปลี่ยนรูปภาพในเว็บ---------------------
    const productContainer1 = document.getElementById("product-container1");

    const inputBtn = document.querySelectorAll("button");
    const clearBtn = document.getElementById("clear-btn");
    const inputBtn1 = document.querySelector(".custom-button6");
    const inputBtn2 = document.querySelector(".custom-button5");
    const inputBtn3 = document.querySelector(".custom-button4");

    const row11 = document.getElementById("row11");
    const row12 = document.getElementById("row12");
    const row13 = document.getElementById("row13");
    const row14 = document.getElementById("row14");
    const row15 = document.getElementById("row15");
    const row16 = document.getElementById("row16");
    const row17 = document.getElementById("row17");
    const row18 = document.getElementById("row18");
    const row19 = document.getElementById("row19");
    const row20 = document.getElementById("row20");
    const row21 = document.getElementById("row21");
    const row22 = document.getElementById("row22");
    const row23 = document.getElementById("row23");
    const row24 = document.getElementById("row24");
    const row25 = document.getElementById("row25");
    const row26 = document.getElementById("row26");

    //---------------------------------------ทำการทดสอบ API สำหรับการทำงานผ่าน django   -----------------------------------------------

    //--------------------------------------สำหรับเก็บไว้ในตัวแปร array ------------------------------------------------------
    //let stockAdjustments = [];
    let savedResults = []; // เก็บผลลัพธ์
    let ArrayBarcode = []; // เก็บไว้สำหรับบาร์โค้ด

    let totalItems = []; // เนื่อย่าง
    let totalItems1 = []; // คอหมูย่าง
    let totalItems2 = []; // ไส้อ่อน
    let totalItems3 = []; // ไส้ใหญ่
    let totalItems4 = []; // ซีกโครงหมู
    let totalItems5 = []; // ไหล่หมู
    let totalItems6 = []; // สันนอก
    let totalItems7 = []; // สามชั้น
    let totalItems8 = []; // กระดูกซูป
    let totalItems9 = [];// หมูบด
    let totalItems10 = [];// สันคอ
















    //-----------------------------------------------------------------สำหรับเก็บค่ารวม------------------------------------

    let currentTotal = 0; //หมูกระทะ
    let currentTotal1 = 0; // คอหมูย่าง
    let currentTotal2 = 0; // ไส้อ่อน
    let currentTotal3 = 0;//  ไส้ใหญ่
    let currentTotal4 = 0;//  ซ๊กโครงหมู
    let currentTotal5 = 0;// ไหลหมู
    let currentTotal6 = 0;//  สันนอก
    let currentTotal7 = 0;// สามชั้น
    let currentTotal8 = 0;// กระดูหมูซูป
    let currentTotal9 = 0;// หมูบด


















    let selectedItem = ""; // ตัวแปรสำหรับเก็บสถานะประเภทที่เลือก ("neauyang" หรือ "sankor")

    //---------------------------------------------------------------รายการสินค้า-----------------------------------------

    const cost = firstBlog1.price; //  หมูกะทะ
    const cost1 = firstBlog2.price; // คอหมูย่าง
    const cost2 = firstBlog3.price; // ไส้อ้อน
    const cost3 = firstBlog4.price; // ไส้ใหญ๋
    const cost4 = firstBlog5.price; // ซีโครงหมู
    const cost5 = firstBlog6.price; // สันนอก
    const cost6 = firstBlog7.price; // หมูสามชั้น
    const cost7 = firstBlog8.price; // กระดูกซูป
    const cost8 = firstBlog9.price; // หมูบด
    const cost9 = firstBlog10.price; // สันคอ


    //-------------------------------------------------------------Stockสินค้าคงเหลือ----------------------------------------

    const stockProduct1 = 12; // หมู่กระทะ
    const stockProduct2 = 15; // สำหรับสันคอ

    //-------------------------------------------------------รายการสินค้า--------------------------------------------------

    const description = "เนื้อย่าง";
    const description1 = "สันคอ";

    //------------------------------------------------------------barcode--------------------------------------------------

    const barcode1 = 1; // หมกระทะ
    const barcode2 = 2; //สันคคอ

    //---------------------------------------------------------หน่วยนับ---------------------------------------------------------------

    const unit1 = "Kg"; // หมูกะทะ
    const unit2 = "kg"; // สันคอ

    //--------------------------------------------------------ราคา--------------------------------------------------------

    const price1 = 15; //เนื้อย่าง
    const price2 = 20; // สันคอ

    //----------------------------------------------------การส่งไฟค์แบบ Jason ----------------------------------------------------

    // สิ่งที่ต้องทำการดิ่งมาคือ ชื่อสินค้า, barcode,หน่วยนับ,ราคา,stoc**************

    //------------------------------------ทดลองสำหรับ QR------------------------------------------




// ✅ กำหนดตัวแปรเก็บรายการสินค้า
let stockAdjustments = JSON.parse(localStorage.getItem("stockAdjustments")) || [];

// ✅ ฟังก์ชันเพิ่ม Event Listener สำหรับปุ่มลบ
function addRemoveEvent() {
    document.querySelectorAll(".remove-item").forEach((button) => {
        button.addEventListener("click", function () {
            let row = this.closest("tr");
            let productName = row.querySelector("td:nth-child(3)").textContent.trim(); // เอาชื่อสินค้าแบบ trim

            // ✅ ลบสินค้าจาก stockAdjustments
            stockAdjustments = stockAdjustments.filter(item => item.product !== productName);
            
            console.log("✅ stockAdjustments หลังลบ:", stockAdjustments);

            // ✅ บันทึกค่าใหม่ไปยัง localStorage
            localStorage.setItem("stockAdjustments", JSON.stringify(stockAdjustments));

            // ✅ ลบแถวออกจากตาราง
            row.remove();

            // ✅ อัปเดตยอดรวม
            updateTotalAmount(); 
        });
    });
}

// ✅ ใช้ Event Delegation แทนการผูก Event ทีละปุ่ม (แก้ปัญหากรณีปุ่มถูกสร้างใหม่)
document.addEventListener("click", function (event) {
    if (event.target.classList.contains("remove-item")) {
        let row = event.target.closest("tr");
        let productName = row.querySelector("td:nth-child(3)").textContent.trim();

        // ✅ ลบสินค้าจาก stockAdjustments
        stockAdjustments = stockAdjustments.filter(item => item.product !== productName);
        console.log("✅ stockAdjustments หลังลบ:", stockAdjustments);

        // ✅ บันทึกค่าใหม่ไปยัง localStorage
        localStorage.setItem("stockAdjustments", JSON.stringify(stockAdjustments));

        // ✅ ลบแถวออกจากตาราง
        row.remove();

        // ✅ อัปเดตยอดรวม
        updateTotalAmount();
    }
});

// ✅ ฟังก์ชันอัปเดตยอดรวม
function updateTotalAmount() {
    let totalAmount = stockAdjustments.reduce((sum, item) => sum + item.TotalPrice, 0);
    let totalProfit = stockAdjustments.reduce((sum, item) => sum + item.totalProfit, 0);

    document.getElementById("totalAmount").innerText = `${totalAmount.toLocaleString(undefined, { 
        minimumFractionDigits: 2, 
        maximumFractionDigits: 2 
    })} บาท`;

    console.log("💰 กำไรทั้งหมด:", totalProfit);
    console.log("💵 ราคาสินค้ารวม:", totalAmount);
}

// ✅ โหลด stockAdjustments จาก localStorage เมื่อหน้าโหลด
document.addEventListener("DOMContentLoaded", function () {
    stockAdjustments = JSON.parse(localStorage.getItem("stockAdjustments")) || [];
    updateTotalAmount();
});


  
  




    //---------------------------------------รายการควบคุมต่างๆๆ-----------------------------------------------------
    // ฟังก์ชันแสดงตัวเลข


    //let scannedBarcode =8850382001087 ;
    // let scannedBarcode1 =1234567891012;

    //let barcodeList = [scannedBarcode, scannedBarcode1];


    // API Data

    //let allBarcodes = blogArray.map(product => product.barcode);
    //  console.log("แสดงค่า Barcode",allBarcodes);
    //let scannedBarcode = 8850382001087; // รับค่าบาร์โค้ดจากช่องแสดงผล


    //scannedBarcode = calculatorDisplay.textContent.trim(); // รับค่าที่พิมพ์
    //foundProduct = blogArray.find(product => product.barcode === scannedBarcode ||product.barcode ===1234567891012); // ค้นหาสินค้าใหม่




    // เก็บบาร์โค้ดทั้งหมดในอาร์เรย์


    // รับค่าบาร์โค้ดที่พิมพ์
    //let scannedBarcode = 1234567891012;

    // 🔥 ต้องกำหนดค่าเริ่มต้นของ `foundProduct` ก่อนใช้
    //let foundProduct = blogArray.find(product => product.barcode === scannedBarcode);

    // 🔍 ตรวจสอบว่าพบสินค้าหรือไม่
    //if (!foundProduct) {
    //console.log("❌ ไม่พบสินค้าในระบบ! กรุณาตรวจสอบบาร์โค้ดอีกครั้ง");
    //alert("❌ ไม่พบสินค้าในระบบ! กรุณาตรวจสอบบาร์โค้ดอีกครั้ง");
    //} else {
    //  console.log("✅ พบสินค้าแล้ว!", foundProduct);
    // console.log("📌 ชื่อสินค้า:", foundProduct.name);
    // console.log("📌 ราคา:", foundProduct.price);
    //console.log("📌 บาร์โค้ด:", foundProduct.barcode);
    //}








    function setNumberValue(number) {


      const displayVlave = calculatorDisplay.textContent; // เก็บตัวแปรการแสดงผลข้อมูลไว้ที่ displayValue
      calculatorDisplay.textContent =
        displayVlave === "0" ? number : displayVlave + number; //ตั้งค่าเป็น 0 เริ่มต้นเมื่อมีการกดก็จะทำการบวกตัวแปรนับเบอร์เข้าไป

      console.log("Current number:", calculatorDisplay.textContent);




    }

    //การควบคุมเกี่ยวกับจุดทศนิยมถ้ากด "."เมื่อทำการกดก็จะให้ตัวเลข 0 มันมาอยู่ข้างหน้า
    function addDecimal() {
      if (!calculatorDisplay.textContent.includes(".")) {
        // สามารถทำการกดจุดได้แค่ครั้งเดียวไม่สามารถทำการกดจุดได้อีกแล้ว
        calculatorDisplay.textContent = `${calculatorDisplay.textContent}.`;
      }
      console.log("addDeciml :", calculatorDisplay.textContent);
    }

    // ฟังก์ชันจัดการโอเปอเรเตอร์
    function callperator(call) {
      console.log(call);
    }

    function Delete() {
      console.log("Display cleared"); // ตรวจสอบเมื่อมีการรีเซ็ตค่า
      calculatorDisplay.textContent = "0"; // รีเซ็ตหน้าจอเป็น 0
    }

    // เพิ่ม Event Listener ให้กับปุ่มทั้งหมด
    inputBtn.forEach((input) => {
      if (input.classList.length === 2) {
        //ลองเช็คตัวจำนวณของ class ว่ามีทั้งหมดกี่ class แล้วทำการเรียกใช้ class ที่ 2
        input.addEventListener("click", () => setNumberValue(input.value)); // ต้องเป็น.value
      } else if (input.classList.contains("operrator")) {
        input.addEventListener("click", () => callperator(input.value));
      } else if (input.classList.contains("delete")) {
        input.addEventListener("click", () => Delete());
      } else if (input.classList.contains("operrator1")) {
        input.addEventListener("click", () => addDecimal());
      }

      console.log(input.classList); // ทำการตรวจสอบclass ที่ประกาศในตัวแปรinput ว่ามันมีทั้งกี่ตัวสำหรับการเรียกใช้งาน input
      console.log(input.classList.length); // ทำการเรียกดูว่ามีclass ที่ความยาว 3 มีทั้้งหมดกี่ตัว
    });

    // ปุ่ม Clear
    clearBtn.addEventListener("click", () => Delete()); // ลบข้อมูลทั้งหมดเมื่อกดปุ่ม Clear

    //--------------------------function สำหรับการเรียกใช้งานใน Keybord----------------------------------------------------

    document.addEventListener("keydown", (event) => {
      const key = event.key; // ดึงค่าปุ่มที่กด
      console.log("Key Pressed:", key);

      // กดตัวเลข
      if (!isNaN(key)) {
        setNumberValue(key); // ส่งตัวเลขไปแสดงผล
      }
      // กดจุดทศนิยม
      else if (key === ".") {
        addDecimal();
      }
      // กด Backspace เพื่อลบตัวเลข
      else if (key === "Backspace") {
        const currentDisplay = calculatorDisplay.textContent;
        calculatorDisplay.textContent = currentDisplay.slice(0, -1) || "0"; // ลบตัวเลขตัวสุดท้าย
        console.log(
          "Backspace pressed, new display:",
          calculatorDisplay.textContent
        );
      }
      // กด ESC เพื่อเคลียร์หน้าจอ
      else if (key === "Escape") {
        Delete();
      }
      // กด Enter เพื่อคำนวณ (หรืออาจเรียกฟังก์ชันอื่น)
      else if (key === "Enter") {
        console.log("Enter key pressed (you can call a calculation function here).");

        // 📌 ตรวจสอบว่า calculatorDisplay มีอยู่จริง
        if (!calculatorDisplay) {
          console.error("❌ calculatorDisplay ไม่ได้ถูกกำหนด!");
          return;
        }

        // 📌 ตรวจสอบค่า calculatorDisplay ก่อนนำไปใช้
        console.log("🔍 ค่า calculatorDisplay.textContent ก่อน trim:", calculatorDisplay.textContent);
        let scannedBarcode = calculatorDisplay.textContent.trim();
        console.log("🔍 ค่า scannedBarcode หลัง trim:", scannedBarcode);

        if (!scannedBarcode) {
          console.log("❌ scannerDisplay.textContent ว่างเปล่า! ไม่สามารถดำเนินการต่อได้");
          return;
        }

        // ✅ ตรวจสอบว่า blogArray มีสินค้าอยู่หรือไม่
        if (!Array.isArray(blogArray)) {
          console.error("❌ blogArray ไม่ได้ถูกกำหนด หรือไม่ใช่ Array!");
          return;
        }

        // ✅ ค้นหาสินค้าใน blogArray
        foundProduct = blogArray.find(product => product.barcode.toString() === scannedBarcode);

        if (!foundProduct) {
          alert("❌ คุณไม่ได้ทำการกรอกตัว barcode ในระบบ.");
          console.log("❌ ไม่พบสินค้าในระบบ! แต่จะไปทำงานในส่วนอื่นต่อ...");
        } else {
          console.log("✅ พบสินค้าแล้ว!", foundProduct);

          // ตรวจสอบว่าตัวแปรถูกกำหนดไว้ก่อนหรือไม่
          if (typeof ArrayBarcode === "undefined") ArrayBarcode = [];
          if (typeof stockAdjustments === "undefined") stockAdjustments = [];
          if (typeof ArrayBarcode1 === "undefined") ArrayBarcode1 = [];
          if (typeof itemtCouter === "undefined") itemtCouter = 0;

          // 🛒 เพิ่มสินค้าในตารางหรืออัปเดตจำนวน
          const tableBody = document.getElementById("itemTableBody");
          const rows = tableBody.querySelectorAll("tr");
          let found = false;

          let Price1 = parseFloat(foundProduct.price) || 0;
          let profitprice = parseFloat(foundProduct.profitprice) || 0;
          let addedQuantity = 1; // จำนวนที่เพิ่มเข้ามาเริ่มต้นเป็น 1
          let totalProfit = profitprice * addedQuantity;
          let TotalPrice = Price1 * addedQuantity;

          rows.forEach((row) => {
            const productCell = row.querySelector("td:nth-child(3)");
            const quantityCell = row.querySelector("td:nth-child(5)");
            const priceCell = row.querySelector("td:nth-child(6)");

            if (productCell && productCell.textContent === foundProduct.name) {
              const currentQuantity = parseFloat(quantityCell.textContent.split(" ")[0]) || 0;
              const newQuantity = currentQuantity + 1;
              const newTotalPrice = newQuantity * foundProduct.price;

              quantityCell.textContent = `${newQuantity} `;
              priceCell.textContent = `${newTotalPrice.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`;

              const adjustmentIndex = stockAdjustments.findIndex(item => item.product === foundProduct.name);
              if (adjustmentIndex > -1) {
                stockAdjustments[adjustmentIndex].quantity += 1;
                stockAdjustments[adjustmentIndex].TotalPrice = stockAdjustments[adjustmentIndex].quantity * foundProduct.price;
                stockAdjustments[adjustmentIndex].totalProfit = stockAdjustments[adjustmentIndex].quantity * foundProduct.profitprice;
              }

              ArrayBarcode.push(foundProduct.price);
              found = true;
              console.log("✅ อัปเดตสินค้าที่มีอยู่ในตารางแล้ว!");
            }
          });

          if (!found) {
            console.log("🔄 เพิ่มสินค้าใหม่เข้าไปในตาราง...");

            ArrayBarcode.push(foundProduct.price);
            addRowToTable(
              itemtCouter,
              foundProduct.barcode,
              foundProduct.name,
              "pcs",
              1,
              foundProduct.price,
              foundProduct.stock
            );

            stockAdjustments.push({
              product: foundProduct.name,
              quantity: 1,
              totalProfit: totalProfit,
              TotalPrice: TotalPrice,
            });

            itemtCouter++;
          }

          const existingProduct = ArrayBarcode1.find(item => item.name === foundProduct.name);
          if (existingProduct) {
            existingProduct.price += Number(foundProduct.price);
            console.log(`🔄 เพิ่มราคาให้สินค้า "${foundProduct.name}" เป็น ${existingProduct.price} บาท`);
          } else {
            ArrayBarcode1.push({ name: foundProduct.name, price: Number(foundProduct.price) });
            console.log(`✅ เพิ่มสินค้าใหม่ "${foundProduct.name}" (ราคา ${foundProduct.price} บาท)`);
          }

          console.log("✅ ค่า ArrayBarcode1 ที่อัปเดตแล้ว:", ArrayBarcode1);

          const grandTotalPrice = stockAdjustments.reduce((sum, item) => sum + item.TotalPrice, 0);
          const grandTotalProfit = stockAdjustments.reduce((sum, item) => sum + item.totalProfit, 0);

          ArrayBarcode = ArrayBarcode.map(Number);
          console.log("✅ ArrayBarcode ที่แปลงเป็นตัวเลขแล้ว:", ArrayBarcode);

          const totalAmount = ArrayBarcode.reduce((sum, item) => sum + Number(item), 0);
          document.getElementById("totalAmount").innerText = `${totalAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`;

          console.log("📦 Stock Adjustments:", stockAdjustments);
          console.log("รวมทั้งหมดสำหรับการสแกนบาร์โค้ด ", ArrayBarcode);
          console.log("💰 Grand Total:", totalAmount);
          console.log("🛒 รวมราคาขายทั้งหมด:", grandTotalPrice);
          console.log("💰 รวมกำไรรวมทั้งหมด:", grandTotalProfit);

          calculatorDisplay.textContent = "0";
          selectedItem = "";
          // ✅ ตรวจสอบว่ามีสินค้าอยู่ก่อนแสดงผล
          if (foundProduct) {
            if (foundProduct.image) {
              productContainer.innerHTML = `
              <div class="img2">
                  <img src="${foundProduct.image}" alt="${foundProduct.name}" />
              </div>`;
            } else {
              productContainer.innerHTML = `<div class="img2">ไม่มีรูปภาพ</div>`;
            }

            productContainer1.innerHTML = `
              <h6>
                  - สินค้าใน stock: ${foundProduct.stock} pcs <br />
                  - ชื่อสินค้า: ${foundProduct.name} <br />
                  - ราคา: ${foundProduct.price} บาท <br />
              </h6>
          `;
          } else {
            productContainer.innerHTML = `<div class="img2">ไม่มีข้อมูลสินค้า</div>`;
            productContainer1.innerHTML = `<h6>ไม่พบข้อมูลสินค้า</h6>`;
          }
        }

        calculatorDisplay.textContent = "0"; // รีเซ็ตค่าแสดงผลเป็น 0
        selectedItem = ""; // รีเซ็ตสถานะหลังจากเพิ่มรายการ



      }
      // กดเครื่องหมายการคำนวณ (+, -, *, /)
      else if (["+", "-", "*", "/"].includes(key)) {
        callperator(key); // เรียกฟังก์ชันโอเปอเรเตอร์
      }
    });



    //-------------------การลบรายการที่เพิ่มเข้าไปในตารางต้องทำการ ศีกษาให้ระเอียด้วยในส่วนนี้เพราะว่าจะป็นการที่เราจะเอาไปใช้ประโยชน์ในโปรเจคถัดไปได้ง่าย ------------------------------

    //------------------------------------------ การเพิ่มการรับเงิน ----------------------------------------------



    //------------------------------------------------------------------สำหรับบาร์โค้ด---------------------------------------------------------

    function colom11() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal = cost * displayVlave; // คำนวณค่า currentTotal ของเนื้อย่าง
      let currency = `${firstBlog1.name} : ${currentTotal.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog1.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "neauyang"; // กำหนดสถานะเป็นเนื้อย่าง
      let imgID = 1;
      console.log("เลือกเนื้อย่าง:", currentTotal);

      if (firstBlog1) {
        productContainer.innerHTML = `
<div class="img2">
<img src="${firstBlog1.image}" alt="${firstBlog1.name}" />
 </div> 
 `;
      }
      if (firstBlog2) {
        productContainer1.innerHTML = `
            <h6>
               -สินค้าใน stock :${firstBlog1.stock} kg <br />
               -ชื่อสินค้า : :${firstBlog1.name} <br />
               -ราคา :${firstBlog1.price} บาท <br />
           </h6>
 `;
      }
    }
    if (row11) {
      row11.addEventListener("click", () => colom11());
    }

    //----------------------------สันคอ----------------------------------------
    function comlum12() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal1 = cost1 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog2.name} : ${currentTotal1.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog2.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "sankor"; // กำหนดสถานะเป็นสันคอ
      console.log("เลือกสันคอ:", currentTotal1);

      if (firstBlog2) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog2.image}" alt="${firstBlog2.name}" />
     </div> 
     `;
      }
      if (firstBlog2) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog2.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog2.name} <br />
                   -ราคา :${firstBlog2.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row12) {
      row12.addEventListener("click", () => comlum12()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย
    }
    //---------------------------------------------ไส้อ้อน-------------------------------------------------

    function comlum13() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal2 = cost2 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog3.name} : ${currentTotal2.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog3.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "SaiOn"; // กำหนดสถานะเป็นสันคอ
      console.log("ไส้อ่อน:", currentTotal2);

      if (firstBlog3) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog3.image}" alt="${firstBlog3.name}" />
     </div> 
     `;
      }
      if (firstBlog3) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog3.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog3.name} <br />
                   -ราคา :${firstBlog3.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row13) {
      row13.addEventListener("click", () => comlum13()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย
    }


    //--------------------------------------------------------------ไส้ใหญ่-----------------------------------------------------


    function comlum14() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal3 = cost3 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog4.name} : ${currentTotal3.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog4.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "SaiYai"; // กำหนดสถานะเป็นสันคอ
      console.log("ไส้ใหญ่:", currentTotal3);

      if (firstBlog4) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog4.image}" alt="${firstBlog4.name}" />
     </div> 
     `;
      }
      if (firstBlog4) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog4.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog4.name} <br />
                   -ราคา :${firstBlog4.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row14) {
      row14.addEventListener("click", () => comlum14()); //
    }



    //-------------------------------------------------------------ซี่โครงหมู-------------------------------------------------------


    function comlum15() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal4 = cost4 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog5.name} : ${currentTotal4.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog5.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "SiKhorongMu"; // กำหนดสถานะเป็นสันคอ
      console.log("ซี่โครงหมู:", currentTotal4);

      if (firstBlog5) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog5.image}" alt="${firstBlog5.name}" />
     </div> 
     `;
      }
      if (firstBlog5) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog5.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog5.name} <br />
                   -ราคา :${firstBlog5.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row15) {
      row15.addEventListener("click", () => comlum15()); // 
    }






    //-------------------------------------------------------------ไหลหมู-------------------------------------------------------




    function comlum17() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal5 = cost5 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog6.name} : ${currentTotal5.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog6.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "LaiMu"; // กำหนดสถานะเป็นสันคอ
      console.log("ซี่โครงหมู:", currentTotal5);

      if (firstBlog6) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog6.image}" alt="${firstBlog6.name}" />
     </div> 
     `;
      }
      if (firstBlog6) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog6.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog6.name} <br />
                   -ราคา :${firstBlog6.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row17) {
      row17.addEventListener("click", () => comlum17()); // 
    }

    //-------------------------------------------------------------สันนอก-------------------------------------------------------



    function comlum18() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal6 = cost6 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog7.name} : ${currentTotal6.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog7.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "SanNok"; // กำหนดสถานะเป็นสันคอ
      console.log("สันนอก:", currentTotal5);

      if (firstBlog7) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog7.image}" alt="${firstBlog7.name}" />
     </div> 
     `;
      }
      if (firstBlog7) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog7.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog7.name} <br />
                   -ราคา :${firstBlog7.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row18) {
      row18.addEventListener("click", () => comlum18()); // 
    }




    //-------------------------------------------------------------สามชั้น-------------------------------------------------------


    function comlum19() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal7 = cost7 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog8.name} : ${currentTotal7.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog8.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "SamChan"; // กำหนดสถานะเป็นสันคอ
      console.log("สามชั้น:", currentTotal5);

      if (firstBlog8) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog8.image}" alt="${firstBlog8.name}" />
     </div> 
     `;
      }
      if (firstBlog8) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog8.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog8.name} <br />
                   -ราคา :${firstBlog8.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row19) {
      row19.addEventListener("click", () => comlum19()); // 
    }




    //-------------------------------------------------------------กระดูกหมูชูป-------------------------------------------------------




    function comlum20() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal8 = cost8 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog9.name} : ${currentTotal8.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog9.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "KradukChup"; // กำหนดสถานะเป็นสันคอ
      console.log("กระดูกหมูชุป:", currentTotal5);

      if (firstBlog9) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog9.image}" alt="${firstBlog9.name}" />
     </div> 
     `;
      }
      if (firstBlog9) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog9.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog9.name} <br />
                   -ราคา :${firstBlog9.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row20) {
      row20.addEventListener("click", () => comlum20()); // 
    }



    //-------------------------------------------------------------หมูบด------------------------------------------------------------



    function comlum21() {
      const displayVlave = calculatorDisplay.textContent;
      currentTotal9 = cost9 * displayVlave; // คำนวณค่า currentTotal ของสันคอ
      let currency = `${firstBlog10.name} : ${currentTotal9.toLocaleString(
        undefined,
        { minimumFractionDigits: 2, maximumFractionDigits: 2 }
      )} บาท 1kg=${firstBlog10.price} บาท `;
      document.getElementById("currency").innerText = currency;
      selectedItem = "MuBot"; // กำหนดสถานะเป็นสันคอ
      console.log("หมูบด:", currentTotal5);

      if (firstBlog10) {
        productContainer.innerHTML = `
    <div class="img2">
    <img src="${firstBlog10.image}" alt="${firstBlog10.name}" />
     </div> 
     `;
      }
      if (firstBlog10) {
        productContainer1.innerHTML = `
                <h6>
                   -สินค้าใน stock :${firstBlog10.stock} Kg <br />
                   -ชื่อสินค้า : :${firstBlog10.name} <br />
                   -ราคา :${firstBlog10.price} บาท <br />
               </h6>
     `;
      }
    }

    if (row21) {
      row21.addEventListener("click", () => comlum21()); // 
    }

    //--------------------------***************เมื่อทำการกดปุ่มรับเงินให้มาแสดงในรายการนี้*****************------------------------------------------

    let enteredAmount = 0; // ตัวแปรสำหรับเก็บตัวเลขที่ผู้ใช้ป้อน




    //************************************************************************************* */
    let ValueSelect = [];  // ✅ เปลี่ยนจาก const เป็น let

    // ✅ รับ Event จาก ajax.js และอัปเดต stockAdjustments
    document.addEventListener("updateStock", function (event) {
      stockAdjustments = event.detail;
      console.log("📦 stockAdjustments ที่ได้รับใน script.js:", stockAdjustments);

      ValueSelect = [...stockAdjustments]; // ✅ ทำสำเนา stockAdjustments ไปยัง ValueSelect
      console.log("📌 ประกาศตัวแปร Global:", ValueSelect);

      if (stockAdjustments.length === 0) {
        console.warn("⚠️ ไม่มีสินค้าใน stockAdjustments");
        return;
      }
      updateCartTable(); // ✅ อัปเดตตารางสินค้า

      // ✅ ทำให้แน่ใจว่า stockAdjustments มีค่า ก่อนอัปเดต Stock
      setTimeout(() => {
        updateStockAPI();
      }, 500); // หน่วงเวลา 0.5 วินาที
    });





    console.log("📤 กำลังส่งข้อมูลไป API:", JSON.stringify({ updates: stockAdjustments }));
    console.log("📦 ค่า stockAdjustments ก่อนส่ง:", stockAdjustments);


    //*************************************************************************************** */





    function amount1() {
      /// แก้bug ก่อน
      // รายการรวมหมูกะทะ--------------------------------------------------
      const displayVlave = calculatorDisplay.textContent; // ทำการประกาศตัวแปรสำหรับการแสดงการเรียกค่าเรียกค่า diaplay เข้ามาแสดง
      let sumNeauyang = totalItems.reduce((sum, current) => sum + current, 0); // ทำการรวมค่าทั้งหมดที่มีสำหรับเนื้อย่าง
      console.log("ราคารวมของเนื้อย่างทั้งหมด:", sumNeauyang); // 720
      // บวกราคารวมของคอหมูย่าง---------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumSankor = totalItems1.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumSankor); // 450
      // บวกราคารวมของไส้อ้อน------------------------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumSaiOn = totalItems2.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumSaiOn); // 450
      // บวกราคารวมของไส้ใหญ่---------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumSaiYai = totalItems3.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumSaiYai); // 450
      // บวกราคารวมของซีครงหมู------------------------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumSiKhorongMu = totalItems4.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumSiKhorongMu); // 450
      // บวกราคารวมของไหล่หมู-----------------------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumLaiMu = totalItems5.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumLaiMu); // 450
      // บวกราคารวมของสั้นนอก-------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumSanNok = totalItems6.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumSanNok); // 450
      // บวกราคารวมของสามชั้น---------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumSamChan = totalItems7.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumSamChan); // 450
      // บวกราคารวมของกระดูกชูป--------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumKradukChup = totalItems8.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumKradukChup); // 450
      // บวกราคารวมของหมูบด--------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumMomot = totalItems9.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumMomot); // 450
      // บวกราคารวมของหมูบด--------------------------------------------------
      enteredAmount = parseFloat(displayVlave); // แปลงค่าที่ป้อนเป็นตัวเลข และเก็บในตัวแปร enteredAmount
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);
      let sumSanCoi = totalItems10.reduce((sum, current) => sum + current, 0); //ทำการรวมค่าทั้งหมดที่มีสำหรับสันคอ
      console.log("ราคารวมของสันคอทั้งหมด:", sumSanCoi); // 450




      //----------------------------------------------------ArrayBarcode---------------------------

      enteredAmount = parseFloat(displayVlave);
      console.log("จำนวนเงินที่ป้อน:", enteredAmount);

      // ตรวจสอบค่าที่อยู่ใน Array ก่อนรวม
      console.log("🔍 ตรวจสอบค่าใน ArrayBarcode1:", ArrayBarcode1);

      // รวมค่าทั้งหมดที่มีอยู่ใน ArrayBarcode
      // ✅ ดึงเฉพาะ price แล้วรวมทั้งหมด
      let totalPrice1 = ArrayBarcode1.reduce((sum, item) => sum + Number(item.price), 0);

      // ✅ แสดงผลรวมของราคา
      console.log("💰 ราคารวมของสินค้า:", totalPrice1.toLocaleString(undefined, {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }));

      //-----------------------------------------------------สำหรับการเลือกจาก dashborad--------------------------------------
       
      // คำนวณผลรวม totalProfit

      let TotalPriceSum = ValueSelect.reduce((sum, item) => sum + item.TotalPrice, 0);
      console.log("📊 ผลรวมของ totalProfit:", TotalPriceSum);








      //---------------------------------------รายการวมทั่งหมดเมื่อมีการทำการกดตรงนี้ ------------------------------------------
      const All = sumNeauyang + sumSankor + sumSaiOn + sumSaiYai + sumSiKhorongMu + sumLaiMu + sumSanNok + sumSamChan + sumKradukChup + sumMomot + totalPrice1+TotalPriceSum;
      console.log("กดได้แล้วน่ะ :", All);





      //------------------------------------------------- ตรวจสอบค่าที่ป้อน----------------------------------------------------------
      if (displayVlave === "0") {
        alert("คุณต้องป้อนตัวเลขที่รับเงินก่อน");
        console.log("คุณต้องป้อนตัวเลขที่รับเงินก่อน");
      } else if (enteredAmount < All) {
        alert(
          `จำนวนเงินที่ป้อนต้องไม่น้อยกว่าราคาสินค้ารวม (${All.toLocaleString()} บาท)`
        );
        console.log("จำนวนเงินที่ป้อนน้อยกว่าราคาสินค้ารวม");
      } else {





        // แสดงผลรวมในหน้าเว็บ


        //---------------------------------------------ที่เรียกทั้งหมดที่อยู่ 1 ตัว-------------------------------------------------------------

        document.querySelectorAll("button").forEach(btn => {
          if (btn.id !== "row22" && !btn.classList.contains("print-btn")) { // ยกเว้นปุ่ม Clean
            btn.style.pointerEvents = "none"; // ❌ ปิดการใช้งานปุ่มแบบไม่ปิด Event โคตเท่สำหรับโปรแกรมการทำงาน 
            btn.style.opacity = "0.4"; // 💡 ทำให้ปุ่มดูเหมือน Disabled
            btn.addEventListener("click", function (event) {
              event.preventDefault(); // ❌ ป้องกันปุ่มทำงาน
              event.stopImmediatePropagation(); // ❌ ป้องกัน Event อื่นที่เกี่ยวข้อง
              alert("⚠️ กรุณากดปุ่ม Clean ก่อนเพื่อทำการปลดล็อก 🔓");
            });
          }
        });




        // ส่งข้อมูลจาก ajax.js เข้ามา






        fetch("http://127.0.0.1:8080/update-stock/", {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken // เพิ่ม CSRF Token ถ้าจำเป็น
          },
          credentials: "include",  // ✅ อนุญาตให้ส่ง Cookies ไปด้วย
          body: JSON.stringify({ updates: stockAdjustments }),
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
          })
          .then((data) => {
            console.log("✅ Stock updated successfully:", data);

            savedResults.push({
              totalAmount: All,
              enteredAmount: enteredAmount,
              change: getMonney,
              stockAdjustments: [...stockAdjustments],
              timestamp: new Date().toISOString(),
            });




            setTimeout(() => {
              fetch("http://127.0.0.1:8080/save-sale-record/", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": csrfToken,
                },
                credentials: "include",
                body: JSON.stringify(savedResults[savedResults.length - 1]),
              })
                .then(response => response.json())
                .then(data => {


                  console.log("✅ Data received:", data);

                  if (data.totalAmount) {

                    console.log("✅ totalAmount:", data.totalAmount);
                    console.log("✅ enteredAmount:", data.enteredAmount);
                    console.log("✅ change:", data.change);
                    console.log("✅ totalAmount:", data.totalAmount);

                    let enteredAmount = parseFloat(data.enteredAmount || 0);
                    let change = parseFloat(data.change || 0);
                    let totalAmount = parseFloat(data.totalAmount || 0);

                    // ✅ อัปเดตค่าบน UI
                    document.getElementById("totalAmount").innerText = totalAmount.toFixed(2) + " บาท";
                    document.getElementById("enteredAmount").innerText = enteredAmount.toFixed(2) + " บาท";
                    document.getElementById("change").innerText = change.toFixed(2) + " บาท";
                    document.getElementById("timestamp").innerText = new Date(data.timestamp).toLocaleString("th-TH");

                    // ✅ แก้ไขการคำนวณให้ถูกต้อง
                    let calculatedTotal = enteredAmount - change;
                    document.getElementById("TotalAmount1").innerText = calculatedTotal.toFixed(2) + " บาท";

                    console.log("✅ Calculated TotalAmount1:", calculatedTotal);

                    // ✅ วนลูปแสดงรายการสินค้า
                    let stockList = document.getElementById("stockAdjustments");
                    stockList.innerHTML = ""; // เคลียร์ข้อมูลเก่า
                    data.stockAdjustments.forEach(item => {
                      let row = `<tr>
                          <td>${item.product}</td>
                          <td>${parseFloat(item.quantity).toFixed(2)}</td>
                          <td>${parseFloat(item.TotalPrice).toFixed(2)} บาท</td>
                      </tr>`;
                      stockList.innerHTML += row;
                    });

                    console.log("✅ Updated UI successfully!");
                  } else {
                    console.error("❌ No totalAmount found in response!");
                  }
                })
                .catch(error => console.error("❌ Error fetching data:", error));

            }, 1000);



            //-------------------------------------ขอทำการโน็ตไว้ก่อนน่ะ


            // แสดงผลรวมในหน้าเว็บ

            // ✅ แสดงปุ่ม "🧾 ดูใบเสร็จ"
            document.getElementById("receiptBtn").style.display = "block";
            // ✅ เปิดป๊อปอัปอัตโนมัติ
            openModal();
            console.log("✅ ผ่านเงื่อนไข แสดงป๊อปอัปใบเสร็จ");




            //-------------------------------------ขอทำการโน็ตไว้ก่อนน่ะ

            console.log("บันทึกผลลัพธ์สำเร็จ:", savedResults);
            console.log("บันทึกผลลัพธ์สำเร็จ:", savedResults);

          })
          .catch((error) => {
            console.error("Error updating stock:", error);
          });
        console.log("CSRF Token:", csrfToken);


        //-----------------------------------------------สำหรับการแสดงผลบนหน้าจอทั้งหมดเมื่อมีการคลิกจ่ายตัง-------------------------
        let getMonney = enteredAmount - All;

        document.getElementById("totalAmount").innerText = `${All.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`; // ทำการแปลงให้เป็นจุดทศนิยม 2 ตำแหน่ง
        document.getElementById("getMonney").innerText = `${enteredAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2, })}บาท`; // ทำการแปลงให้เป็นจุดทศนิยม 2 ตำแหน่ง
        document.getElementById("withDraw").innerText = `${getMonney.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2, })} บาท`; // ทำการแปลงให้เป็นจุดทศนิยม 2 ตำแหน่ง



        //------------------------------------------------สำหรับการแสดง Qr โค้ดพร้อมเพย์---------------------------------------


        const phone = "0624380985"; // เบอร์ PromptPay
        const amount = 100.00; // จำนวนเงิน

        fetch(`/generate-promptpay-qr/?phone_number=${phone}&amount=${All}`)
          .then(response => response.json())
          .then(data => {
            if (data.qr_code) {
              const qrImage = document.getElementById("qrCodeImage");
              qrImage.src = `data:image/png;base64,${data.qr_code}`;
              qrImage.style.display = "block"; // แสดงรูปภาพ QR Code
            } else {
              alert(data.error || "Failed to generate QR code.");
            }
          })
          .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while generating QR code.");
          });


        console.log("เงินทอน:", getMonney.toFixed(2), "บาท"); // คำนวณเงินทอน




      }
      calculatorDisplay.textContent = 0; // รีเซ็ตค่า


    }
    if (inputBtn3) {
      inputBtn3.addEventListener("click", () => amount1());
    }


    //----------------------------------------ทำการเพิ่มความปอดภัยโดยใช้ CSRFToken----------------------------------------------
    function getCSRFToken() {
      const cookies = document.cookie.split("; ");
      for (const cookie of cookies) {
        if (cookie.startsWith("csrftoken=")) {
          return cookie.split("=")[1];
        }
      }
      return null;
    }

    const csrfToken = getCSRFToken();
    console.log("CSRF Token:", csrfToken)
    //-----------------------------------------------สำหรับการลบแถวในตาราง------------------------------------------------- */

    function DeleteItem() {



      const tableBody = document.getElementById("itemTableBody"); // ดึง tbody ของตาราง
      if (tableBody && tableBody.lastElementChild) {
        // ดึงแถวสุดท้ายของตาราง
        const lastRow = tableBody.lastElementChild;
        //------------------------------------------------------สำหรับลบตารางหมูกระทะ---------------------------------------------
        if (lastRow) {
          let productType = lastRow.querySelector("td:nth-child(3)")?.textContent; // ชื่อสินค้าในคอลัมน์ที่ 3

          if (productType === firstBlog1.name) {
            // ลบข้อมูลใน stockAdjustments201
            const adjustmentIndex = stockAdjustments.findIndex(
              (item) => item.product === productType    // ใช้ productType แทน productName
            );
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1); //ลบรายการที่เป็นแถวจาก adjustmentIndec
              console.log(`ลบข้อมูลสินค้า: ${productType} ออกจาก stockAdjustments`);

            }
            // ลบแถวออกจากตาราง
            console.log("ลบแถวสำเร็จ");

            totalItems.splice(0, totalItems.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems เนี้อย่าง :", totalItems);



            //-------------------------------------------------------------------สำหรับลบตรารางขอหมูย่าง--------------------------------- 

          } else if (productType === firstBlog2.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }
            totalItems1.splice(0, totalItems1.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems1 คอหมูย่าง :", totalItems1);

            //-------------------------------------------------------------------ไส่อ่อน-----------------------------------
          } else if (productType === firstBlog3.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }



            totalItems2.splice(0, totalItems2.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems2  ไส้อ่อน :", totalItems2);



            //-----------------------------------------------------------------ไส้ใหญ่-------------------------------------------------


          } else if (productType === firstBlog4.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }

            totalItems3.splice(0, totalItems3.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems3 ไส้ใหญ่ :", totalItems3);



            //-------------------------------------------------------------------------------------------------------------------------


          } else if (productType === firstBlog5.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }


            totalItems4.splice(0, totalItems4.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems2 :", totalItems4);



            //------------------------------------------------------------------ไหล่หมู-----------------------------------------




          } else if (productType === firstBlog6.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }
            totalItems5.splice(0, totalItems5.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems2 :", totalItems5);



            //------------------------------------------------------------------ลบสันนอกออก--------------------------------------


          } else if (productType === firstBlog7.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }
            totalItems6.splice(0, totalItems6.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems2 :", totalItems6);


            //-------------------------------------------------------------------ลบสามชั้นออก-------------------------------------------



          } else if (productType === firstBlog8.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }
            totalItems7.splice(0, totalItems7.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems2 :", totalItems7);

            //-------------------------------------------------------------กระดูกชูป-----------------------------------------


          } else if (productType === firstBlog9.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }
            totalItems8.splice(0, totalItems8.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems2 :", totalItems8);



            //----------------------------------------------หมูบด-------------------------------------------


          } else if (productType === firstBlog10.name) {
            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === productType);
            if (adjustmentIndex > -1) {
              stockAdjustments.splice(adjustmentIndex, 1);
              console.log(`ลบข้อมูลสินค้า ${productType} ออกจาก stockAdjustments`)
            }
            totalItems9.splice(0, totalItems9.length);
            console.log("ลบข้อมูลทั้งหมดออกจาก totalItems2 :", totalItems9);

            //-------------------------------------------ArrayBarcode----------------------------------------------------------------- 
          }

        }
      } else {
        console.log("ไม่มีรายการให้ลบ");
        alert("ไม่มีรายการในตารางที่สามารถลบได้");
      }
    }

    if (inputBtn2) {
      inputBtn2.addEventListener("click", () => DeleteItem());
    }


    //-------------------------------------------------------------------------




    //-------------------------------------------------- การลบสำหรับการยิงบาร์โค้ด-----------------------------------------------


    function DeleteLatestItem() {
      const tableBody = document.getElementById("itemTableBody");
      if (!tableBody || !tableBody.lastElementChild) {
        console.log("⚠️ ไม่มีแถวในตารางให้ลบ");
        alert("ไม่มีรายการในตารางที่สามารถลบได้");
        return;
      }

      // ✅ ดึงแถวสุดท้าย
      let lastRow = tableBody.lastElementChild;
      let productType = lastRow.querySelector("td:nth-child(3)")?.textContent.trim();

      if (!productType) {
        console.log("⚠️ ไม่สามารถระบุชื่อสินค้าได้");
        return;
      }

      console.log(`🔍 ลบแถวล่าสุด: "${productType}"`);

      // ✅ ลบสินค้าตัวล่าสุดที่ตรงกันจาก stockAdjustments
      const lastIndex = stockAdjustments.findLastIndex(item => item.product === productType);
      if (lastIndex > -1) {
        let removedItem = stockAdjustments.splice(lastIndex, 1)[0];
        console.log(`❌ ลบสินค้าล่าสุดที่ตรงกันจาก stockAdjustments:`, removedItem);
      } else {
        console.log(`⚠️ ไม่พบสินค้า "${productType}" ใน stockAdjustments`);
      }

      // ✅ ลบสินค้าออกจาก ArrayBarcode1 ด้วย
      const arrayIndex = ArrayBarcode1.findIndex(item => item.name === productType);
      if (arrayIndex > -1) {
        ArrayBarcode1.splice(arrayIndex, 1);
        console.log(`❌ ลบสินค้าจาก ArrayBarcode1: "${productType}"`);
      }

      console.log("📦 Stock Adjustments ปัจจุบัน:", JSON.stringify(stockAdjustments, null, 2));

      // ✅ ลบแถวสุดท้ายจาก tableBody
      tableBody.removeChild(lastRow);
      console.log("✅ ลบแถวสำเร็จ");

      // ✅ ตรวจสอบว่าเหลือสินค้าใน stockAdjustments หรือไม่
      if (stockAdjustments.length > 0) {
        productType = stockAdjustments[stockAdjustments.length - 1].product;
        console.log(`🔄 อัปเดตค่า productType ใหม่เป็น "${productType}"`);
      } else {
        productType = null;
        console.log("🚨 ไม่มีข้อมูลสินค้าเหลืออยู่ใน stockAdjustments แล้ว!");
      }

      // ✅ อัปเดตยอดรวม (Total Amount)
      const totalAmount = stockAdjustments.reduce((sum, item) => sum + item.TotalPrice, 0);
      document.getElementById("totalAmount").innerText = `${totalAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`;
      console.log("💰 อัปเดตยอดรวมหลังลบสินค้า:", totalAmount);
    }










    // ✅ เพิ่ม event listener ให้ปุ่ม
    if (inputBtn2) {
      inputBtn2.addEventListener("click", DeleteLatestItem);
    }














    //-----------------------------------------------------การเพิ่มค่าในตารางเนื้อย่าง-------------------------------------------------------



    function Additem() {
      console.log("🔄 Starting Additem function...");


      // ✅ **รองรับสินค้าแบบ Dynamic**
      let productList = [
        { key: "neauyang", product: firstBlog1, totalItems: totalItems, currentTotal: currentTotal },
        { key: "sankor", product: firstBlog2, totalItems: totalItems1, currentTotal: currentTotal1 },
        { key: "SaiOn", product: firstBlog3, totalItems: totalItems2, currentTotal: currentTotal2 },
        { key: "SaiYai", product: firstBlog4, totalItems: totalItems3, currentTotal: currentTotal3 },
        { key: "SiKhorongMu", product: firstBlog5, totalItems: totalItems4, currentTotal: currentTotal4 },
        { key: "LaiMu", product: firstBlog6, totalItems: totalItems5, currentTotal: currentTotal5 },
        { key: "SanNok", product: firstBlog7, totalItems: totalItems6, currentTotal: currentTotal6 },
        { key: "SamChan", product: firstBlog8, totalItems: totalItems7, currentTotal: currentTotal7 },
        { key: "KradukChup", product: firstBlog9, totalItems: totalItems8, currentTotal: currentTotal8 },
        { key: "MuBot", product: firstBlog10, totalItems: totalItems9, currentTotal: currentTotal9 },


      ];
      let selectedProduct = productList.find(item => item.key === selectedItem);



      if (selectedProduct && selectedProduct.currentTotal > 0) {
        console.log(`🔍 Processing additional item: ${selectedProduct.product.name}`);
        const tableBody = document.getElementById("itemTableBody");
        const rows = tableBody.querySelectorAll("tr");
        let found = false;

        // ✅ คำนวณราคาและกำไร
        let Price1 = parseFloat(selectedProduct.product.price);
        let profitprice = parseFloat(selectedProduct.product.profitprice);
        let addedQuantity = parseFloat(calculatorDisplay.textContent);
        let totalProfit = profitprice * addedQuantity;
        let TotalPrice = Price1 * addedQuantity;

        console.log(`💰 กำไรที่เพิ่มเข้ามา: ${totalProfit.toFixed(2)} บาท`);

        rows.forEach((row) => {
          const productCell = row.querySelector("td:nth-child(3)");
          const quantityCell = row.querySelector("td:nth-child(5)");
          const priceCell = row.querySelector("td:nth-child(6)");

          if (productCell && productCell.textContent === selectedProduct.product.name) {
            const currentQuantity = parseFloat(quantityCell.textContent.split(" ")[0]);
            const newQuantity = currentQuantity + addedQuantity;
            const newTotalPrice = newQuantity * Price1;

            quantityCell.textContent = `${newQuantity} `;
            priceCell.textContent = `${newTotalPrice.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`;

            const adjustmentIndex = stockAdjustments.findIndex((item) => item.product === selectedProduct.product.name);
            if (adjustmentIndex > -1) {
              stockAdjustments[adjustmentIndex].quantity += addedQuantity;
              stockAdjustments[adjustmentIndex].totalProfit += totalProfit;
              stockAdjustments[adjustmentIndex].TotalPrice += TotalPrice;
            }

            selectedProduct.totalItems.push(selectedProduct.currentTotal);
            found = true;
          }
        });

        if (!found) {
          selectedProduct.totalItems.push(selectedProduct.currentTotal);
          addRowToTable(
            itemtCouter,
            selectedProduct.product.barcode,
            selectedProduct.product.name,
            "kg",
            calculatorDisplay.textContent,
            selectedProduct.currentTotal,
            selectedProduct.product.stock
          );

          // ✅ ตรวจสอบว่ามีสินค้าชื่อเดียวกันอยู่ใน stockAdjustments หรือไม่
          const existingItemIndex = stockAdjustments.findIndex(item => item.product === selectedProduct.product.name);
          if (existingItemIndex !== -1) {
            // ✅ หากมีแล้ว ให้อัปเดตจำนวนสินค้าและราคาที่รวมกัน
            stockAdjustments[existingItemIndex].quantity += addedQuantity;
            stockAdjustments[existingItemIndex].totalProfit += totalProfit;
            stockAdjustments[existingItemIndex].TotalPrice += TotalPrice;
          } else {
            // ✅ ถ้ายังไม่มี ให้เพิ่มเป็นสินค้าใหม่
            stockAdjustments.push({
              product: selectedProduct.product.name,
              quantity: addedQuantity,
              totalProfit: totalProfit,
              TotalPrice: TotalPrice
            });
          }
        }

        // ✅ อัปเดตยอดรวม
        const grandTotalPrice = stockAdjustments.reduce((sum, item) => sum + item.TotalPrice, 0);
        const grandTotalProfit = stockAdjustments.reduce((sum, item) => sum + item.totalProfit, 0);
        const grandTotal = selectedProduct.totalItems.reduce((sum, item) => sum + item, 0);
        document.getElementById("totalAmount").innerText = `${grandTotal.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`;

        console.log(`📦 Stock Adjustments (Updated):`, stockAdjustments);
        console.log("💰 รวมกำไรทั้งหมด", grandTotalProfit);
        console.log("💵 รวมราคาทั้งหมด", grandTotalPrice);

        selectedProduct.currentTotal = 0;
      } else {
        console.log("❌ ไม่พบสินค้าใน Product List แต่โค้ดยังคงทำงานต่อ...");
        alert("❌ โปรดเลือกรายสินค้าก่อน");
        console.log("โปรดทำการเพิ่มสินค้าในรายการ");
      }

      calculatorDisplay.textContent = "0"; // รีเซ็ตค่าแสดงผลเป็น 0
      selectedItem = ""; // รีเซ็ตสถานะหลังจากเพิ่มรายการ

    }
    //-------------------------------------------------------- รายการต่อสำหรับการตัด stock -------------------------------------------------------------*
















    //------------------------------------------------------------รายการต่อไปที่จะดึงเข้ามาแสดง-----------------------------------------------------------*

    console.log("รายการที่ต้องการปรับสต็อก:", stockAdjustments);

    // เพิ่ม event listener สำหรับปุ่ม row11 (เนื้อย่าง)
    if (row11) {
      row11.addEventListener("click", () => colom11());
    }

    // เพิ่ม event listener สำหรับปุ่ม row12 (ใส่ค่าสันคอ)
    if (row12) {
      row12.addEventListener("click", () => comlum12());
    }

    if (inputBtn1) {
      inputBtn1.addEventListener("click", () => Additem());
    }

    //------------------------------------------------------******************************--------------------------------------------------






    




    


    let itemtCouter = 1;

function addRowToTable(itemt, barcode, product, kg, count, price, stock1) {
    const tableBody = document.getElementById("itemTableBody"); // ดึง tbody ของตาราง
    const newRow = document.createElement("tr"); // สร้างแถวใหม่

    // สร้าง cell สำหรับลำดับ
    const itemtCell = document.createElement("td");
    itemtCell.textContent = `${itemt}`;
    newRow.appendChild(itemtCell);
    itemtCouter++; // เพิ่มค่าในระบบ

    // สร้างเซลสำหรับชื่อสินค้า
    const barcodeCell = document.createElement("td");
    barcodeCell.textContent = `${barcode}`;
    newRow.appendChild(barcodeCell);

    const productCell = document.createElement("td");
    productCell.textContent = product;
    newRow.appendChild(productCell);

    const kgCell = document.createElement("td");
    kgCell.textContent = kg;
    newRow.appendChild(kgCell);

    const countCell = document.createElement("td");
    countCell.textContent = `${count} `;
    newRow.appendChild(countCell);

    const priceCell = document.createElement("td");
    priceCell.textContent = `${price.toLocaleString(undefined, {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    })} บาท`;
    newRow.appendChild(priceCell);

    const stock1Cell = document.createElement("td");
    stock1Cell.textContent = `${stock1} `;
    newRow.appendChild(stock1Cell);

    const deleteProductCell = document.createElement("td");
    deleteProductCell.innerHTML = `<button type="button" class="btn btn-danger remove-item">ลบข้อมูล</button>`;
    newRow.appendChild(deleteProductCell);

    tableBody.appendChild(newRow);
    

    

    addRemoveEvent(); // เพิ่ม Event Listener ให้กับปุ่มลบทั้งหมด
}


    //----------------------------------------------------************-------------------------------------------




    //-------------------------------------------**********************-----------------------------------

    //--------------------------------------------------------------------


    //-----------------------------------------------------------------

    // ✅ ประกาศตัวแปร foundProduct เป็น global ที่ด้านบน
    let ArrayBarcode1 = [];
    let foundProduct = null;




    // -------------------------------------------------------สำหรับการสแกน-------------------------------------------------------










    /* document.addEventListener("DOMContentLoaded", function () {
       let inputField = document.getElementById("calculatorDisplay");
       let row16Button = document.getElementById("row16"); // ดึงปุ่มที่ต้องการกดอัตโนมัติ
   
       if (!inputField) {
           console.error("❌ ไม่พบ input ที่มี id='calculatorDisplay'");
           return;
       }
   
       if (!row16Button) {
           console.error("❌ ไม่พบปุ่มที่มี id='row16'");
           return;
       }
   
       inputField.addEventListener("input", function () {
           let scannedBarcode = this.value.trim();
           console.log("📌 ตรวจสอบค่า input:", scannedBarcode);
   
           if (/^\d+$/.test(scannedBarcode)) { // ถ้าป้อนเป็นตัวเลข
               console.log("✅ Barcode ถูกต้อง! กดปุ่ม row16...");
               setTimeout(() => {
                   row16Button.click(); // กดปุ่ม row16 อัตโนมัติ
               }, 200);
           }
       });
   });*/



    //------------------------------------สำหรับไม่ต้องสแกนบาร์โคด้-----------------------------
    function comlum16() {
      // 📌 ตรวจสอบค่า calculatorDisplay ก่อนนำไปใช้
      console.log("🔍 ค่า calculatorDisplay.textContent ก่อน trim:", calculatorDisplay.textContent);
      let scannedBarcode = calculatorDisplay.textContent.trim();
      console.log("🔍 ค่า scannedBarcode หลัง trim:", scannedBarcode);

      if (!scannedBarcode) {
        console.log("❌ scannerDisplay.textContent ว่างเปล่า! ไม่สามารถดำเนินการต่อได้");
        return;
      }

      // ✅ อัปเดตค่า foundProduct ใหม่
      foundProduct = blogArray.find(product => product.barcode.toString() === scannedBarcode);

      if (!foundProduct) {
        alert("❌ คุณไม่ได้ทำการกรอกตัว barcode ในระบบ.");
        console.log("❌ ไม่พบสินค้าในระบบ! แต่จะไปทำงานในส่วนอื่นต่อ...");
      } else {
        console.log("✅ พบสินค้าแล้ว!", foundProduct);

        // 🛒 เพิ่มสินค้าในตารางหรืออัปเดตจำนวน
        const tableBody = document.getElementById("itemTableBody");
        const rows = tableBody.querySelectorAll("tr");
        let found = false;

        // ✅ ดึงราคาสินค้า และกำไรต่อหน่วย (ProfitPrice)
        let Price1 = parseFloat(foundProduct.price);
        let profitprice = parseFloat(foundProduct.profitprice);
        let addedQuantity = 1; // จำนวนที่เพิ่มเข้ามาเริ่มต้นเป็น 1

        // ✅ คำนวณกำไร = profitprice * quantity
        let totalProfit = profitprice * addedQuantity;

        // ✅ คำนวณราคาขายรวม
        let TotalPrice = Price1 * addedQuantity;

        rows.forEach((row) => {
          const productCell = row.querySelector("td:nth-child(3)");
          const quantityCell = row.querySelector("td:nth-child(5)");
          const priceCell = row.querySelector("td:nth-child(6)");

          if (productCell && productCell.textContent === foundProduct.name) {
            const currentQuantity = parseFloat(quantityCell.textContent.split(" ")[0]);
            const newQuantity = currentQuantity + 1;
            const newTotalPrice = newQuantity * foundProduct.price;

            quantityCell.textContent = `${newQuantity} `;
            priceCell.textContent = `${newTotalPrice.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`;

            const adjustmentIndex = stockAdjustments.findIndex(item => item.product === foundProduct.name);
            if (adjustmentIndex > -1) {
              stockAdjustments[adjustmentIndex].quantity += 1;
              stockAdjustments[adjustmentIndex].TotalPrice = stockAdjustments[adjustmentIndex].quantity * foundProduct.price;
              stockAdjustments[adjustmentIndex].totalProfit = stockAdjustments[adjustmentIndex].quantity * foundProduct.profitprice;
            }

            ArrayBarcode.push(Number(foundProduct.price));
            found = true;
            console.log("✅ อัปเดตสินค้าที่มีอยู่ในตารางแล้ว!");
          }
        });

        if (!found) {
          console.log("🔄 เพิ่มสินค้าใหม่เข้าไปในตาราง...");

          ArrayBarcode.push(Number(foundProduct.price));
          addRowToTable(
            itemtCouter,
            foundProduct.barcode,
            foundProduct.name,
            "pcs",
            1,
            foundProduct.price,
            foundProduct.stock
          );

          // ✅ ตรวจสอบว่ามีสินค้าชื่อเดียวกันอยู่ใน stockAdjustments หรือไม่
          const existingProduct = stockAdjustments.find(item => item.product === foundProduct.name);
          if (existingProduct) {
            // ✅ หากมีแล้ว ให้อัปเดตจำนวนสินค้าและราคาที่รวมกัน
            existingProduct.quantity += addedQuantity;
            existingProduct.totalProfit += totalProfit;
            existingProduct.TotalPrice += TotalPrice;
          } else {
            // ✅ ถ้ายังไม่มี ให้เพิ่มเป็นสินค้าใหม่
            stockAdjustments.push({
              product: foundProduct.name, // ✅ ใช้ foundProduct.name แทน selectedProduct
              quantity: addedQuantity,
              totalProfit: totalProfit,
              TotalPrice: TotalPrice
            });
          }

          itemtCouter++;
        }

        // ✅ ตรวจสอบ ArrayBarcode1
        const existingProduct1 = ArrayBarcode1.find(item => item.name === foundProduct.name);
        if (existingProduct1) {
          existingProduct1.price += Number(foundProduct.price);
          console.log(`🔄 เพิ่มราคาให้สินค้า "${foundProduct.name}" เป็น ${existingProduct1.price} บาท`);
        } else {
          ArrayBarcode1.push({ name: foundProduct.name, price: Number(foundProduct.price) });
          console.log(`✅ เพิ่มสินค้าใหม่ "${foundProduct.name}" (ราคา ${foundProduct.price} บาท)`);
        }

        console.log("✅ ค่า ArrayBarcode1 ที่อัปเดตแล้ว:", ArrayBarcode1);

        const grandTotalPrice = stockAdjustments.reduce((sum, item) => sum + item.TotalPrice, 0);
        const grandTotalProfit = stockAdjustments.reduce((sum, item) => sum + item.totalProfit, 0);

        // ✅ แปลงราคาทั้งหมดเป็นตัวเลข
        ArrayBarcode = ArrayBarcode.map(Number);
        console.log("✅ ArrayBarcode ที่แปลงเป็นตัวเลขแล้ว:", ArrayBarcode);

        // 🔢 **คำนวณ Total Items และแสดงผล**
        const totalAmount = ArrayBarcode.reduce((sum, item) => sum + Number(item), 0);
        document.getElementById("totalAmount").innerText = `${totalAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} บาท`;

        console.log("📦 Stock Adjustments:", stockAdjustments);
        console.log("💰 รวมกำไรรวมทั้งหมด:", grandTotalProfit);
        console.log("🛒 รวมราคาขายทั้งหมด:", grandTotalPrice);

        calculatorDisplay.textContent = "0";
        selectedItem = "";



        //-----------------------------------------


        //-------------------------------------------------------------------------------------

        // ✅ ตรวจสอบว่ามีสินค้าอยู่ก่อนแสดงผล
        if (foundProduct) {
          if (foundProduct.image) {
            productContainer.innerHTML = `
                <div class="img2">
                    <img src="${foundProduct.image}" alt="${foundProduct.name}" />
                </div>`;
          } else {
            productContainer.innerHTML = `<div class="img2">ไม่มีรูปภาพ</div>`;
          }

          productContainer1.innerHTML = `
                <h6>
                    - สินค้าใน stock: ${foundProduct.stock} pcs <br />
                    - ชื่อสินค้า: ${foundProduct.name} <br />
                    - ราคา: ${foundProduct.price} บาท <br />
                </h6>
            `;
        } else {
          productContainer.innerHTML = `<div class="img2">ไม่มีข้อมูลสินค้า</div>`;
          productContainer1.innerHTML = `<h6>ไม่พบข้อมูลสินค้า</h6>`;
        }
      }

      calculatorDisplay.textContent = "0"; // รีเซ็ตค่าแสดงผลเป็น 0
      selectedItem = ""; // รีเซ็ตสถานะหลังจากเพิ่มรายการ
    }

    if (row16) {
      row16.addEventListener("click", () => comlum16()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย

    }


    console.log("ว่ามันจะเกิดไรขึ้นหลังจากนี้", foundProduct);
    console.log("ทดสอบ api การทำงาน", ArrayBarcode)

    //-------------------------------สำหรับ pop up Ajax -----------------------------------













































    //--------------------------------ปุ่มเคลียร-------------------------
    function comlum22() {

      fetch("http://127.0.0.1:8080/Dashboard/", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
      })
        .then(response => {
          if (response.ok) {
            console.log("row22");
            // รีเฟรชหน้าเว็บหลังจาก fetch สำเร็จ
            window.location.reload();
          } else {
            console.error("Error:", response.statusText);
          }
        })
        .catch(error => {
          console.error("Fetch error:", error);
        });


    }

    if (row22) {
      row22.addEventListener("click", () => comlum22()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย
    }

    //--------------------------------------------------------------------
    function comlum23() {
      console.log("row23");
    }

    if (row23) {
      row23.addEventListener("click", () => comlum23()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย
    }

    //--------------------------------------------------------------------
    function comlum24() {
      console.log("row24");
    }

    if (row24) {
      row24.addEventListener("click", () => comlum24()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย
    }

    //--------------------------------------------------------------------
    function comlum25() {
      console.log("row25");
    }

    if (row25) {
      row25.addEventListener("click", () => comlum25()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย
    }

    //--------------------------------------------------------------------
    function comlum26() {
      console.log("row26");
    }

    if (row26) {
      row26.addEventListener("click", () => comlum26()); // ใช้เป็น id แทนระบุแต่ล่ะตัวไปเลย
    }
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });




////-------------------------------------function ทดสอบ API สำหรับการทำงาน---------------------------------------





