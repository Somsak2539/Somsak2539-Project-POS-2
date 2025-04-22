/*
Template Name: StarCode & Dashboard Template
Author: StarCode Kh
Version: 1.1.0
Website: https://StarCode Kh.in/
Contact: StarCode Kh@gmail.com
File: dashboard analytics init Js File
*/

// rgb to hex convert
function rgbToHex(rgb) {
    // Extract RGB values using regular expressions
    const rgbValues = rgb.match(/\d+/g);

    if (rgbValues.length === 3) {
        var [r, g, b] = rgbValues.map(Number);
    }
    // Ensure the values are within the valid range (0-255)
    r = Math.max(0, Math.min(255, r));
    g = Math.max(0, Math.min(255, g));
    b = Math.max(0, Math.min(255, b));

    // Convert each component to its hexadecimal representation
    const rHex = r.toString(16).padStart(2, '0');
    const gHex = g.toString(16).padStart(2, '0');
    const bHex = b.toString(16).padStart(2, '0');

    // Combine the hexadecimal values with the "#" prefix
    const hexColor = `#${rHex}${gHex}${bHex}`;

    return hexColor.toUpperCase(); // Convert to uppercase for consistency
}

// common function to get charts colors from class
function getChartColorsArray(chartId) {
    const chartElement = document.getElementById(chartId);
    if (chartElement) {
        const colors = chartElement.dataset.chartColors;
        if (colors) {
            const parsedColors = JSON.parse(colors);
            const mappedColors = parsedColors.map((value) => {
                const newValue = value.replace(/\s/g, "");
                if (!newValue.includes("#")) {
                    const element = document.querySelector(newValue);
                    if (element) {
                        const styles = window.getComputedStyle(element);
                        const backgroundColor = styles.backgroundColor;
                        return backgroundColor || newValue;
                    } else {
                        const divElement = document.createElement('div');
                        divElement.className = newValue;
                        document.body.appendChild(divElement);

                        const styles = window.getComputedStyle(divElement);
                        const backgroundColor = styles.backgroundColor.includes("#") ? styles.backgroundColor : rgbToHex(styles.backgroundColor);
                        return backgroundColor || newValue;
                    }
                } else {
                    return newValue;
                }
            });
            return mappedColors;
        } else {
            console.warn(`chart-colors attribute not found on: ${chartId}`);
        }
    }
}

//********************************************************รายรับและรายจ่าย---------------------------------------------





function loadSalesChart(type) {
    fetch("/indexDashboardUser/?format=json")
        .then(response => response.json())
        .then(data => {
            let salesData, profitData, categories;

           
            
            if (type === 'daily') {
                salesData = data.daily_sales.map(item => parseFloat(item.total).toFixed(2));
                profitData = data.daily_profit1.map(item => parseFloat(item.total).toFixed(2)); // ✅ แก้ให้เก็บค่าต่อเนื่อง
                categories = data.daily_sales.map(item => item.date);

            } else if (type === 'weekly') {
                salesData = data.weekly_sales.map(item => parseFloat(item.total).toFixed(2));
                profitData = data.weekly_profit1.map(item => parseFloat(item.total).toFixed(2)); // ✅ แก้ไข
                categories = data.weekly_sales.map(item => "สัปดาห์ที่ " + item.week);

            } else if (type === 'monthly') {
                salesData = data.monthly_sales.map(item => parseFloat(item.total).toFixed(2));
                profitData = data.monthly_profit1.map(item => parseFloat(item.total).toFixed(2)); // ✅ แก้ไข
                categories = data.monthly_sales.map(item => "เดือน " + item.month);
            }


            console.log("แสดงค่าsaleData",salesData);
            console.log("แสดงค่าProfitData",profitData);

            var options = {
                series: [
                    { name: "ยอดขายรวม (บาท)", data: salesData },
                    { name: "กำไรรวม (บาท)", data: profitData } // ✅ เพิ่มเส้นกำไร
                ],
                chart: { height: 350, type: 'line', zoom: { enabled: false }, toolbar: { show: false } },
                stroke: { curve: 'smooth', width: 2 },
                dataLabels: { enabled: false },
                colors: ["#4CAF50", "#FF5733"], // ✅ สีของกราฟ (ยอดขาย = เขียว, กำไร = แดง)
                xaxis: { categories: categories, title: { text: "ช่วงเวลา" } },
                yaxis: { 
                    title: { text: "มูลค่า (บาท)" },
                    labels: {
                        formatter: function (value) {
                            return (value || 0).toFixed(2); // ✅ แสดงค่าเป็นทศนิยม 2 ตำแหน่ง
                        }
                    }
                },
                legend: { position: "top" }
            };

            document.querySelector("#responseTimes").innerHTML = "";
            var chart = new ApexCharts(document.querySelector("#responseTimes"), options);
            chart.render();
        })
        .catch(error => console.error("❌ Error fetching sales data:", error));
}

// ✅ โหลดกราฟเริ่มต้น (รายวัน)
loadSalesChart('daily');

// ✅ เปลี่ยนประเภทกราฟเมื่อคลิกปุ่ม
document.querySelector("#dailyBtn").addEventListener("click", () => loadSalesChart('daily'));
document.querySelector("#weeklyBtn").addEventListener("click", () => loadSalesChart('weekly'));
document.querySelector("#monthlyBtn").addEventListener("click", () => loadSalesChart('monthly'));



//********************************************************รายรับและรายจ่าย---------------------------------------------



function loadSalesChart11(type) {
    fetch("/indexDashboardUser/?format=json")
        .then(response => response.json())
        .then(data => {
            let salesData, profitData, categories;

           
            
            if (type === 'daily') {
                salesData = data.daily_sales.map(item => parseFloat(item.total).toFixed(2));
                profitData = data.daily_profit1.map(item => parseFloat(item.total).toFixed(2)); // ✅ แก้ให้เก็บค่าต่อเนื่อง
                categories = data.daily_sales.map(item => item.date);

            } else if (type === 'weekly') {
                salesData = data.weekly_sales.map(item => parseFloat(item.total).toFixed(2));
                profitData = data.weekly_profit1.map(item => parseFloat(item.total).toFixed(2)); // ✅ แก้ไข
                categories = data.weekly_sales.map(item => "สัปดาห์ที่ " + item.week);

            } else if (type === 'monthly') {
                salesData = data.monthly_sales.map(item => parseFloat(item.total).toFixed(2));
                profitData = data.monthly_profit1.map(item => parseFloat(item.total).toFixed(2)); // ✅ แก้ไข
                categories = data.monthly_sales.map(item => "เดือน " + item.month);
            }


            console.log("แสดงค่าsaleData",salesData);
            console.log("แสดงค่าProfitData",profitData);

            var options = {
                series: [
                    { name: "ยอดขายรวม (บาท)", data: salesData },
                    { name: "กำไรรวม (บาท)", data: profitData } // ✅ เพิ่มเส้นกำไร
                ],
                chart: { height: 350, type: 'line', zoom: { enabled: false }, toolbar: { show: false } },
                stroke: { curve: 'smooth', width: 2 },
                dataLabels: { enabled: false },
                colors: ["#4CAF50", "#FF5733"], // ✅ สีของกราฟ (ยอดขาย = เขียว, กำไร = แดง)
                xaxis: { categories: categories, title: { text: "ช่วงเวลา" } },
                yaxis: { 
                    title: { text: "มูลค่า (บาท)" },
                    labels: {
                        formatter: function (value) {
                            return (value || 0).toFixed(2); // ✅ แสดงค่าเป็นทศนิยม 2 ตำแหน่ง
                        }
                    }
                },
                legend: { position: "top" }
            };

            document.querySelector("#responseTimes11").innerHTML = "";
            var chart = new ApexCharts(document.querySelector("#responseTimes11"), options);
            chart.render();
        })
        .catch(error => console.error("❌ Error fetching sales data:", error));
}

// ✅ โหลดกราฟเริ่มต้น (รายวัน)
loadSalesChart11('daily');

// ✅ เปลี่ยนประเภทกราฟเมื่อคลิกปุ่ม
document.querySelector("#dailyBtn11").addEventListener("click", () => loadSalesChart11('daily'));
document.querySelector("#weeklyBtn11").addEventListener("click", () => loadSalesChart11('weekly'));
document.querySelector("#monthlyBtn11").addEventListener("click", () => loadSalesChart11('monthly'));





























/*function loadSalesChart() {
    fetch("/indexDashboardUser/?format=json")  // ✅ เรียก API Django
        .then(response => response.json())
        .then(data => {
            let salesData = data.product_sales.map(item => item.y);  // ✅ ดึงยอดขายแต่ละสินค้า
            let categories = data.product_sales.map(item => item.x); // ✅ ดึงชื่อสินค้า

            var options = {
                series: [{
                    name: "ยอดขาย (กก.)",
                    data: salesData
                }],
                chart: {
                    height: 350,
                    type: 'line',
                    zoom: { enabled: false },
                    toolbar: { show: false }
                },
                stroke: {
                    curve: 'smooth',
                    width: 2
                },
                dataLabels: {
                    enabled: false
                },
                colors: ["#4CAF50"],  // ✅ สีเส้นกราฟ
                xaxis: {
                    categories: categories // ✅ ชื่อสินค้าในแกน X
                }
            };

            // ✅ ล้างข้อมูลเก่า แล้วสร้างกราฟใหม่
            document.querySelector("#responseTimes").innerHTML = "";
            var chart = new ApexCharts(document.querySelector("#responseTimes"), options);
            chart.render();
        })
        .catch(error => console.error("Error fetching sales data:", error));
}

// ✅ โหลดกราฟตอนเปิดหน้า
loadSalesChart();*/
        
/*var options = {
    series: [{
        name: "Response Times",
        data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
    }],
    chart: {
        height: 350,
        type: 'line',
        zoom: {
            enabled: false
        },
        margin: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0
        },
        toolbar: {
            show: false,
        },
    },
    stroke: {
        show: true,
        curve: 'smooth',
        lineCap: 'butt',
        width: 2,
        dashArray: 0,
    },
    dataLabels: {
        enabled: false
    },
    colors: getChartColorsArray("responseTimes"),
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
    }
};

var chart = new ApexCharts(document.querySelector("#responseTimes"), options);
chart.render();*/



//Pages Interaction






// กราฟแสดงรายรับแต่ล่ะเดือน

document.addEventListener("DOMContentLoaded", function () {
    function fetchSalesData(type) {
        console.log("🟢 กำลังเรียก API: /indexDashboardUser/?format=json");

        fetch("/indexDashboardUser/?format=json")
            .then(response => response.json())
            .then(data => {
                console.log("✅ ข้อมูล JSON ที่ได้รับ:", data);

                let salesData, profitData, categories;

                if (type === 'daily') {
                    salesData = data.daily_sales.map(item => parseFloat(item.total).toFixed(2));
                    profitData = data.daily_profit1.map(item => parseFloat(item.total).toFixed(2));
                    // ตัดเวลาและโซนเวลาออก (รูปแบบ ISO: "2025-02-17T00:00:00+07:00")
                    categories = data.daily_sales.map(item => item.date.split('T')[0]);

                } else if (type === 'weekly') {
                    salesData = data.weekly_sales.map(item => parseFloat(item.total).toFixed(2));
                    profitData = data.weekly_profit1.map(item => parseFloat(item.total).toFixed(2));
                    
                    // สร้างป้ายชื่อสัปดาห์พร้อมช่วงวันที่
                    categories = data.weekly_sales.map(item => {
                        const weekDate = new Date(item.week);
                        const weekNumber = getWeekNumber(weekDate);
                        const [startDate, endDate] = getWeekDateRange(weekDate);
                        return `สัปดาห์ที่ ${weekNumber} (${formatDateRange(startDate, endDate)})`;
                    });

                } else if (type === 'monthly') {
                    salesData = data.monthly_sales.map(item => parseFloat(item.total).toFixed(2));
                    profitData = data.monthly_profit1.map(item => parseFloat(item.total).toFixed(2));
                    // แปลง month เป็น "เดือน YYYY-MM"
                    categories = data.monthly_sales.map(item => {
                        const monthDate = new Date(item.month);
                        const year = monthDate.getFullYear();
                        const month = String(monthDate.getMonth() + 1).padStart(2, '0');
                        return `เดือน ${year}-${month}`;
                    });
                }

                console.log("📊 ข้อมูลยอดขายสำหรับกราฟ pagesInteraction:", salesData);
                console.log("📆 ข้อมูลวันที่สำหรับกราฟ pagesInteraction:", categories);

                updateChart(salesData, categories);
            })
            .catch(error => console.error("❌ เกิดข้อผิดพลาด:", error));
    }

    // ฟังก์ชันคำนวณสัปดาห์
    function getWeekNumber(date) {
        const d = new Date(date);
        d.setHours(0, 0, 0, 0);
        d.setDate(d.getDate() + 4 - (d.getDay() || 7));
        const yearStart = new Date(d.getFullYear(), 0, 1);
        const weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
        return weekNo;
    }


 // ฟังก์ชันหาช่วงวันที่ของสัปดาห์ (เริ่มต้นวันอาทิตย์)
 function getWeekDateRange(date) {
    const start = new Date(date);
    start.setDate(start.getDate() - start.getDay()); // เริ่มวันอาทิตย์
    const end = new Date(start);
    end.setDate(end.getDate() + 6); // สิ้นสุดวันเสาร์
    return [start, end];
}



// ฟังก์ชันจัดรูปแบบวันที่ (เช่น "17-23 Feb 2025")
function formatDateRange(start, end) {
    const options = { day: 'numeric', month: 'short', year: 'numeric' };
    const startStr = start.toLocaleDateString('en-US', options).replace(',', '');
    const endStr = end.toLocaleDateString('en-US', options).replace(',', '');
    return `${startStr.split(' ')[0]}-${endStr}`;
}

    // ฟังก์ชันแสดงกราฟ (เหมือนเดิม)
    function updateChart(salesData, categories) {
        var options = {
            series: [{
                name: 'ยอดขายรวม (บาท)',
                data: salesData
            }],
            chart: { height: 350, type: 'bar', toolbar: { show: false } },
            plotOptions: { bar: { borderRadius: 10, dataLabels: { position: 'top' } } },
            dataLabels: { 
                enabled: true,
                offsetY: -20,
                style: { fontSize: '12px', colors: ["#304758"] }
            },
            xaxis: { 
                categories: categories,
                title: { text: "วันที่" },
                tooltip: { enabled: true }
            },
            yaxis: { 
                title: { text: "มูลค่า (บาท)" },
                labels: { formatter: val => `${val.toLocaleString()} บาท` }
            },
            stroke: { show: true, width: 4, colors: ['transparent'] },
            grid: { show: false },
            colors: ["#4CAF50"]
        };

        document.querySelector("#pagesInteraction").innerHTML = "";
        var chart = new ApexCharts(document.querySelector("#pagesInteraction"), options);
        chart.render();
    }

    fetchSalesData('weekly'); // โหลดข้อมูลเริ่มต้น
});



//*******************************************รายการสินค้าขายดี รวมยอดขายทั้งหมดที่ขายไปแล้ว
// เรียกใช้ API เพื่อดึงข้อมูลยอดขาย
/*fetch("/indexDashboardUser/?format=json")
    .then(response => response.json())
    .then(data => {
        let salesDataMap = {}; // ใช้ Object เก็บข้อมูลสินค้าแบบรวม

        // วนลูปผ่านรายการขาย
        data.sales.forEach(item => {
            item.stock_adjustments.forEach(sale => {
                let productName = sale.product || "ไม่ทราบชื่อ"; // ใช้ชื่อสินค้า

                if (salesDataMap[productName]) {
                    salesDataMap[productName] += sale.quantity; // ถ้าซ้ำให้บวกยอด kg
                } else {
                    salesDataMap[productName] = sale.quantity; // ถ้าไม่ซ้ำให้ตั้งค่าเริ่มต้น
                }
            });
        });

        // แปลง Object เป็น Array ที่ ApexCharts ใช้ได้
        let salesData = Object.keys(salesDataMap).map(product => ({
            x: product,
            y: salesDataMap[product]
        }));


        // รับค่าข้อมูลสินค้าแบบ JSON ที่ผ่านการกรองจาก Django
           
        
        // สร้าง Chart ใหม่โดยใช้ข้อมูลที่ดึงมา
        var options = {
            series: [{ data: salesData }],
            legend: { show: false },
            chart: {
                height: 270,
                type: 'treemap',
                toolbar: { show: false }
            },
            grid: {
                show: false,
                padding: {
                    top: -15,
                    bottom: 0,
                    right: -20
                },
            },
            colors: getChartColorsArray("platformPerspective"),
        };

        // เรนเดอร์ Chart
        var chart = new ApexCharts(document.querySelector("#platformPerspective"), options);
        chart.render();
    })
    .catch(error => console.error("เกิดข้อผิดพลาดในการดึงข้อมูล:", error));*/







//กราฟแสดงรายการที่ขายดีที่สุด



    function loadSalesChart1(filterType) {
        fetch(`/indexDashboardUser/?format=json&filter=${filterType}`) // ✅ ส่งพารามิเตอร์ไป Django
            .then(response => response.json())
            .then(data => {
                let salesDataMap = {}; // ใช้ Object เก็บข้อมูลสินค้าแบบรวม
                let salesRecords = data.sales; // ✅ ใช้ JSON ที่ Django ส่งกลับมา
    
                // ✅ ตรวจสอบว่ามีข้อมูลก่อนใช้ forEach
                if (!salesRecords || !Array.isArray(salesRecords)) {
                    console.error("ไม่มีข้อมูลขาย หรือ JSON ไม่ถูกต้อง:", data);
                    return;
                }
    
                // ✅ วนลูปผ่านรายการขายที่ได้รับการกรองจาก Django
                salesRecords.forEach(item => {
                    if (item.stock_adjustments) {
                        item.stock_adjustments.forEach(sale => {
                            let productName = sale.product || "ไม่ทราบชื่อ"; 
    
                            if (salesDataMap[productName]) {
                                salesDataMap[productName] += sale.quantity;
                            } else {
                                salesDataMap[productName] = sale.quantity;
                            }
                        });
                    }
                });
    
                // ✅ แปลง Object เป็น Array ที่ ApexCharts ใช้ได้
                let salesData = Object.keys(salesDataMap).map(product => ({
                    x: product,
                    y: salesDataMap[product]
                }));
    
                // ✅ สร้าง Chart ใหม่โดยใช้ข้อมูลที่ดึงมา
                var options = {
                    series: [{ data: salesData }],
                    legend: { show: false },
                    chart: {
                        height: 270,
                        type: 'treemap',
                        toolbar: { show: false }
                    },
                    grid: {
                        show: false,
                        padding: { top: -15, bottom: 0, right: -20 }
                    },
                    colors: getChartColorsArray("platformPerspective"),
                    tooltip: {
                        y: {
                            formatter: function(value) {
                                return value.toFixed(2); // ✅ แสดงค่าทศนิยม 2 ตำแหน่ง
                            }
                        }
                    }
                };
    
                // ✅ ล้างข้อมูลเก่าก่อนเรนเดอร์ใหม่
                document.querySelector("#platformPerspective").innerHTML = "";
                var chart = new ApexCharts(document.querySelector("#platformPerspective"), options);
                chart.render();
            })
            .catch(error => console.error("เกิดข้อผิดพลาดในการดึงข้อมูล:", error));
    }
    
    // ✅ โหลดกราฟตอนเปิดหน้า (ค่าเริ่มต้นเป็น 'daily')
    loadSalesChart1('daily');
    






//************************************totalProfit1******************************************************** */

document.addEventListener("DOMContentLoaded", function () {
    function fetchFilteredData(filterType) {
        console.log(`🟢 กำลังเรียก API: /indexDashboardUser/?format=json&filter=${filterType}`);

        fetch(`/indexDashboardUser/?format=json&filter=${filterType}`)
            .then(response => response.json())
            .then(data => {
                console.log(`✅ ข้อมูลที่ได้รับจาก API (${filterType}):`, data);

                // ✅ อัปเดตค่า totalProfit ลงใน HTML
                let totalProfitElement = document.getElementById("totalProfitDisplay");
                if (totalProfitElement) {
                    totalProfitElement.textContent = data.totalProfit1.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                } else {
                    console.error("❌ ไม่พบ <span id='totalProfitDisplay'> ใน DOM");
                }

                // ✅ Debugging: ตรวจสอบค่า JSON ที่ส่งกลับมา
                console.log("🔍 Debugging: JSON Response =", data);
            })
            .catch(error => console.error("❌ เกิดข้อผิดพลาด:", error));
    }

    // ✅ เพิ่ม Event Listener ให้ปุ่มกรองข้อมูล
    document.getElementById("filterDaily2").addEventListener("click", () => fetchFilteredData("day"));
    document.getElementById("filterWeekly2").addEventListener("click", () => fetchFilteredData("week"));
    document.getElementById("filterMonthly2").addEventListener("click", () => fetchFilteredData("month"));
    document.getElementById("filterYearly2").addEventListener("click", () => fetchFilteredData("year"));

    fetchFilteredData("day");  // ✅ โหลดค่าเริ่มต้นเป็น "รายวัน"
});

//************************************totalPrice******************************************************** */




document.addEventListener("DOMContentLoaded", function () {
    function fetchFilteredData(filterType) {
        console.log(`🟢 กำลังเรียก API: /indexDashboardUser/?format=json&filter=${filterType}`);

        fetch(`/indexDashboardUser/?format=json&filter=${filterType}`)
            .then(response => response.json())
            .then(data => {
                console.log(`✅ ข้อมูลที่ได้รับจาก API (${filterType}):`, data);

                // ✅ อัปเดตค่า totalProfit ลงใน HTML
                let totalProfitElement = document.getElementById("total_sum");
                if (totalProfitElement) {
                    totalProfitElement.textContent = data.total_sum.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                } else {
                    console.error("❌ ไม่พบ <span id='total'> ใน DOM");
                }

                // ✅ Debugging: ตรวจสอบค่า JSON ที่ส่งกลับมา
                console.log("🔍 Debugging: JSON Response =", data);
            })
            .catch(error => console.error("❌ เกิดข้อผิดพลาด:", error));
    }

    // ✅ เพิ่ม Event Listener ให้ปุ่มกรองข้อมูล
    document.getElementById("filterDaily2").addEventListener("click", () => fetchFilteredData("day"));
    document.getElementById("filterWeekly2").addEventListener("click", () => fetchFilteredData("week"));
    document.getElementById("filterMonthly2").addEventListener("click", () => fetchFilteredData("month"));
    document.getElementById("filterYearly2").addEventListener("click", () => fetchFilteredData("year"));

    fetchFilteredData("day");  // ✅ โหลดค่าเริ่มต้นเป็น "รายวัน"
});






    

//*********************************************************User Devices
var options = {
    series: [{
        name: 'Desktop',
        data: [80, 50, 30, 40, 100, 20],
    }, {
        name: 'Mobile',
        data: [20, 30, 40, 80, 20, 80],
    }, {
        name: 'Others',
        data: [44, 76, 78, 13, 43, 10],
    }],
    chart: {
        height: 240,
        type: 'radar',
        dropShadow: {
            enabled: true,
            blur: 1,
            left: 1,
            top: 1
        },
        toolbar: {
            show: false,
        }
    },
    stroke: {
        width: 2
    },
    fill: {
        opacity: 0.1
    },
    markers: {
        size: 0
    },
    responsive: [{
        breakpoint: 480,
        options: {
            legend: {
                show: false
            }
        }
    }],
    colors: getChartColorsArray("userDeviceCharts"),
    legend: {
        position: 'right',
        offsetY: 0,
        height: 230,
    },
    xaxis: {
        categories: ['2018', '2019', '2020', '2021', '2022', '2023']
    }
};

var chart = new ApexCharts(document.querySelector("#userDeviceCharts"), options);
chart.render();

//Satisfaction Rate
var options = {
    series: [95.33],
    chart: {
        type: 'radialBar',
        height: 450,
        offsetY: -20,
        sparkline: {
            enabled: true
        }
    },
    plotOptions: {
        radialBar: {
            startAngle: -90,
            endAngle: 90,
            track: {
                strokeWidth: '97%',
                margin: 5, // margin is in pixels
            },
            hollow: {
                size: '60%',
                margin: 0,
                image: '../../assets/images/logo-sm.png',
                imageWidth: 36,
                imageHeight: 36,
                imageClipped: false,
                imageOffsetY: -60,
            },
            dataLabels: {
                name: {
                    show: false
                },
                value: {
                    offsetY: -5,
                    fontSize: '22px',
                    fontWeight: '600'
                }
            }
        }
    },
    grid: {
        padding: {
            top: -10
        }
    },
    colors: getChartColorsArray("satisfactionRate"),
    fill: {
        type: 'gradient',
        gradient: {
            shade: 'light',
            shadeIntensity: 0.4,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 50, 53, 91]
        },
    },
    stroke: {
        dashArray: 4
    },
    labels: ['Average Results'],
};

var chart = new ApexCharts(document.querySelector("#satisfactionRate"), options);
chart.render();

//Daily Visit Insights
var options = {
    series: [
        {
            name: 'Male',
            data: [55, 41, 67, 22, 43, 21, 33, 45]
        },
        {
            name: 'Female',
            data: [55, 41, 67, 22, 43, 21, 33, 45]
        }
    ],
    annotations: {
        points: [{
            x: 'Bananas',
            seriesIndex: 0,
            label: {
                borderColor: getChartColorsArray("dailyVisitInsightsChart")[1],
                offsetY: 0,
                style: {
                    color: '#fff',
                    background: getChartColorsArray("dailyVisitInsightsChart")[1],
                },
                text: 'Bananas are good',
            }
        }]
    },
    colors: getChartColorsArray("dailyVisitInsightsChart"),
    chart: {
        height: 238,
        type: 'bar',
        toolbar: {
            show: false,
        }
    },
    plotOptions: {
        bar: {
            borderRadius: 10,
            columnWidth: '70%',
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 2
    },
    xaxis: {
        labels: {
            rotate: -45
        },
        categories: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        tickPlacement: 'on'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shade: 'light',
            type: "horizontal",
            shadeIntensity: 0.25,
            gradientToColors: undefined,
            inverseColors: true,
            opacityFrom: 0.85,
            opacityTo: 0.85,
            stops: [50, 0, 100]
        },
    },
    grid: {
        xaxis: {
            lines: {
                show: true
            }
        },
        yaxis: {
            lines: {
                show: true
            }
        },
        padding: {
            top: -10,
            right: -10,
            left: -10
        }
    },
    yaxis: {
        show: false,
    }
};

var chart = new ApexCharts(document.querySelector("#dailyVisitInsightsChart"), options);
chart.render();

//Subscription Distribution
var options = {
    series: [44, 55, 41, 17, 15],
    labels: ['Beginner', 'Intermediate', 'Enterprise', 'VIP', 'Professional'],
    chart: {
        height: 270,
        type: 'donut',
    },
    plotOptions: {
        pie: {
            startAngle: -90,
            donut: {
                size: '75%'
            }
        }
    },
    dataLabels: {
        enabled: false
    },
    fill: {
        type: 'gradient',
    },
    colors: getChartColorsArray("subscriptionDistribution"),
    legend: {
        formatter: function (val, opts) {
            return val + " - " + opts.w.globals.series[opts.seriesIndex]
        }
    },
    legend: {
        position: 'bottom'
    }
};

var chart = new ApexCharts(document.querySelector("#subscriptionDistribution"), options);
chart.render();

// Line with Data Labels
var dataLabelOptions = {
    series: [
        {
            name: "Income - 2023",
            data: [28, 29, 33, 36, 32]
        },
        {
            name: "Expense - 2023",
            data: [20, 17, 21, 29, 23]
        }
    ],
    chart: {
        height: 235,
        type: 'line',
        dropShadow: {
            enabled: true,
            color: '#000',
            top: 18,
            left: 7,
            blur: 10,
            opacity: 0.2
        },
        toolbar: {
            show: false
        }
    },
    colors: getChartColorsArray("lineWithDataLabel"),
    dataLabels: {
        enabled: true,
    },
    stroke: {
        curve: 'smooth',
        size: 2,
    },
    markers: {
        size: 1
    },
    yaxis: {
      show: false  
    },
    xaxis: {
        categories: ['Mar', 'Apr', 'May', 'Jun', 'Jul'],
    },
    legend: {
        position: 'top',
        horizontalAlign: 'right',
        floating: true,
        offsetY: -25,
        offsetX: -5
    },
    grid: {
        xaxis: {
            lines: {
                show: false
            }
        },
        yaxis: {
            lines: {
                show: false
            }
        },
        padding: {
            top: -25,
        }
    },
};

var chart = new ApexCharts(document.querySelector("#lineWithDataLabel"), dataLabelOptions);
chart.render();