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
    const searchBar = document.querySelector('input[name="q"]');
    if (!searchBar) return;

    // ปุ่มกล้อง
    const scanBtn = document.createElement("button");
    scanBtn.type = "button";
    scanBtn.textContent = "📷 สแกนบาร์โค้ด";
    scanBtn.style.marginLeft = "10px";

    searchBar.parentNode.appendChild(scanBtn);

    scanBtn.addEventListener("click", () => {
        const scannerDiv = document.createElement("div");
        scannerDiv.id = "scanner";
        scannerDiv.style.width = "300px";
        scannerDiv.style.marginTop = "10px";
        searchBar.parentNode.appendChild(scannerDiv);

        const qrScanner = new Html5Qrcode("scanner");

        qrScanner.start(
          { facingMode: "environment" },
          {
            fps: 15,
            qrbox: { width: 250, height: 250 },
            aspectRatio: 1.0,
            disableFlip: true
          },
          (decodedText) => {
            searchBar.value = decodedText;
            qrScanner.stop();
            //document.querySelector('form').submit();
            document.getElementById("scanner").remove();
          },
          (error) => {
            console.log("Scan error:", error);
          
        });
    });
});