document.addEventListener("DOMContentLoaded", function () {
    const barcodeField = document.querySelector("#id_barcode");
  
    if (!barcodeField) return;
  
    // ปุ่มกล้อง
    const scanBtn = document.createElement("button");
    scanBtn.type = "button";
    scanBtn.textContent = "📷 สแกนบาร์โค้ด";
    scanBtn.style.marginLeft = "10px";
  
    barcodeField.parentNode.appendChild(scanBtn);
  
    scanBtn.addEventListener("click", () => {
      const scannerDiv = document.createElement("div");
      scannerDiv.id = "scanner";
      scannerDiv.style.width = "300px";
      scannerDiv.style.marginTop = "10px";
      barcodeField.parentNode.appendChild(scannerDiv);
  
      const qrScanner = new Html5Qrcode("scanner");
      qrScanner.start(
        { facingMode: "environment" },
        { fps: 10, qrbox: 250 },
        (decodedText) => {
          barcodeField.value = decodedText;
          qrScanner.stop();
          scannerDiv.remove();
        }
      );
    });
  });
  


  document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        const searchBar = document.querySelector('input[name="q"]');
        if (!searchBar) return;

        const button = document.createElement("button");
        button.innerText = "📷 สแกนบาร์โค้ด";
        button.type = "button";
        button.style.marginLeft = "10px";
        button.classList.add("btn", "btn-info");

        searchBar.parentNode.appendChild(button);

        // ✅ สร้าง container สำหรับแสดงกล้องแบบเต็มจอ
        const scannerContainer = document.createElement("div");
        scannerContainer.id = "barcode-scanner";
        scannerContainer.style.position = "fixed";
        scannerContainer.style.top = "0";
        scannerContainer.style.left = "0";
        scannerContainer.style.width = "100vw";
        scannerContainer.style.height = "100vh";
        scannerContainer.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
        scannerContainer.style.zIndex = "9999";
        scannerContainer.style.display = "none";
        scannerContainer.style.alignItems = "center";
        scannerContainer.style.justifyContent = "center";
        scannerContainer.style.flexDirection = "column";

        // ✅ สร้าง div สำหรับแสดงกล้อง
        const cameraView = document.createElement("div");
        cameraView.id = "camera-view";
        cameraView.style.width = "90%"; // ใช้ 90% ของความกว้างหน้าจอ
        cameraView.style.maxWidth = "400px"; // กำหนดขนาดสูงสุด
        cameraView.style.height = "auto";
        cameraView.style.aspectRatio = "16 / 9"; // สัดส่วน 16:9 ให้ดูสมมาตร
        cameraView.style.background = "#000";
        scannerContainer.appendChild(cameraView);

        // ✅ ปุ่มปิดกล้อง
        const closeBtn = document.createElement("button");
        closeBtn.innerText = "❌ ปิดกล้อง";
        closeBtn.style.marginTop = "20px";
        closeBtn.style.padding = "10px 20px";
        closeBtn.style.backgroundColor = "#f44336";
        closeBtn.style.color = "#fff";
        closeBtn.style.border = "none";
        closeBtn.style.borderRadius = "5px";
        closeBtn.style.cursor = "pointer";
        closeBtn.addEventListener("click", () => {
            html5QrCode.stop().then(() => {
                scannerContainer.style.display = "none";
            });
        });
        scannerContainer.appendChild(closeBtn);

        document.body.appendChild(scannerContainer);

        const html5QrCode = new Html5Qrcode("camera-view");

        button.addEventListener("click", function () {
            if (scannerContainer.style.display === "none") {
                scannerContainer.style.display = "flex";

                Html5Qrcode.getCameras().then(cameras => {
                    if (cameras && cameras.length > 0) {
                        const cameraId = cameras[0].id;
                        html5QrCode.start(
                            cameraId,
                            {
                                fps: 10,
                                qrbox: { width: 250, height: 100 }
                            },
                            qrCodeMessage => {
                                searchBar.value = qrCodeMessage;
                                html5QrCode.stop().then(() => {
                                    scannerContainer.style.display = "none";
                                    document.querySelector('form[action=""]').submit();
                                });
                            },
                            errorMessage => {
                                console.log("Scan error:", errorMessage);
                            }
                        );
                    } else {
                        alert("ไม่พบกล้องบนอุปกรณ์ค่ะ");
                    }
                }).catch(err => {
                    alert("ไม่สามารถเข้าถึงกล้องได้: " + err);
                });
            } else {
                html5QrCode.stop().then(() => {
                    scannerContainer.style.display = "none";
                });
            }
        });
    }, 500);
});



