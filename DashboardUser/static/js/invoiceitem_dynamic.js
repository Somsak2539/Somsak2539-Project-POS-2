document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('id_category');
    const productSelect = document.getElementById('id_product');

    categorySelect.addEventListener('change', function () {
        const categoryId = this.value;

        fetch(`/ajax/load-products/?category_id=${categoryId}`)
            .then(response => response.json())
            .then(data => {
                // เคลียร์ dropdown เดิม
                productSelect.innerHTML = '';
                const emptyOption = document.createElement('option');
                emptyOption.text = '---------';
                productSelect.appendChild(emptyOption);

                // เพิ่ม options ใหม่
                data.forEach(item => {
                    const option = document.createElement('option');
                    option.value = item.id;
                    option.text = item.name;
                    productSelect.appendChild(option);
                });
            });
    });
});
