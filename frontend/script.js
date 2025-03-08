let selectedSuggestion = null;

document.getElementById('imageUpload').addEventListener('change', function(e) {
    const file = e.target.files[0];
    const preview = document.getElementById('previewImage');
    const previewIcon = document.getElementById('previewIcon');
    const previewText = document.getElementById('previewText');
    const resultText = document.getElementById('resultText');

    if (file) {
        const imageUrl = URL.createObjectURL(file);
        preview.src = imageUrl;
        preview.style.display = 'block'; // Show uploaded image
        preview.style.opacity = '0'; // Start with fade-in effect
        previewIcon.style.display = 'none'; // Hide camera icon
        previewText.style.display = 'none'; // Hide preview text
        setTimeout(() => preview.style.opacity = '1', 50); // Fade in
        
        resultText.innerHTML = '<p>Đang chờ phân tích...</p>';
        selectedSuggestion = null; // Reset suggestion when uploading new image
    } else {
        // Reset if no file is selected
        preview.style.display = 'none';
        previewIcon.style.display = 'block';
        previewText.style.display = 'block';
        resultText.textContent = 'Tải ảnh để xem kết quả';
    }
});

function analyzeImage() {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];
    const resultText = document.getElementById('resultText');

    if (!file) {
        alert('Vui lòng tải ảnh lên trước!');
        return;
    }

    resultText.innerHTML = '<p class="loading">Đang phân tích...</p>';

    const formData = new FormData();
    formData.append('image', file);
    if (selectedSuggestion) {
        formData.append('suggestion', selectedSuggestion);
    }

    fetch('/analyze', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server trả về lỗi: ${response.status} - ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) throw new Error(data.error);

        resultText.innerHTML = `
            <div class="analysis-result">
                <h3>Nhan sắc:</h3>
                <ul>${data.nhan_sac?.map(item => `<li>${item}</li>`).join('') || '<li>Không có dữ liệu</li>'}</ul>
                <h3>Thời trang:</h3>
                <ul>${data.fashion?.map(item => `<li>${item}</li>`).join('') || '<li>Không có dữ liệu</li>'}</ul>
                
            </div>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        resultText.innerHTML = '<p class="error">Có lỗi xảy ra: ' + error.message + '. Vui lòng thử lại.</p>';
    });
}

document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        const filter = this.getAttribute('data-filter');
        document.querySelectorAll('.gallery-item').forEach(item => {
            const category = item.getAttribute('data-category');
            item.style.display = (filter === 'all' || category === filter) ? 'block' : 'none';
        });
    });
});

document.querySelectorAll('.gallery-item img').forEach(img => {
    img.addEventListener('click', function() {
        // const preview = document.getElementById('previewImage');
        // const previewIcon = document.getElementById('previewIcon');
        // const previewText = document.getElementById('previewText');
        const resultText = document.getElementById('resultText');

        // preview.src = this.src;
        // preview.style.display = 'block'; // Show preview image
        // preview.style.opacity = '0'; // Start with fade-in effect
        // previewIcon.style.display = 'none'; // Hide camera icon
        // previewText.style.display = 'none'; // Hide preview text
        selectedSuggestion = this.nextElementSibling.textContent || 'Phong cách mẫu';
        resultText.textContent = `Gợi ý đã chọn: ${selectedSuggestion}. Nhấn "Phân tích Ngay" để áp dụng.`;

        setTimeout(() => preview.style.opacity = '1', 50); // Fade in
    });
});