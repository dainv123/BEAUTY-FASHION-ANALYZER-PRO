beauty_suggestions = {
    "bright_skin": ["Duy trì chăm sóc da tốt.", "Thử son màu cam hoặc hồng đào."],
    "dark_skin": ["Dùng kem dưỡng sáng da.", "Thử son đỏ đậm để nổi bật."],
    "oily_skin": ["Dùng giấy thấm dầu thường xuyên.", "Chọn kem nền kiềm dầu."],
    "young_age": ["Tập trung vào dưỡng ẩm.", "Thử makeup tự nhiên."],
    "mature_age": ["Dùng kem chống lão hóa.", "Thử makeup nhấn mắt."],
    "Trang điểm tự nhiên": ["Dùng phấn má hồng nhẹ.", "Son nude hợp tông da."]
}

fashion_suggestions = {
    "warm_colors": ["Phối với quần tối màu để cân bằng.", "Thử phụ kiện vàng."],
    "cool_colors": ["Phối với áo trắng để nổi bật.", "Thử phụ kiện bạc."],
    "casual_style": ["Thêm giày sneaker trắng.", "Thử áo khoác denim."],
    "formal_style": ["Thêm giày cao gót.", "Thử khăn quàng cổ sang trọng."],
    "Phong cách tối giản": ["Chọn áo sơ mi trắng đơn giản.", "Phối với quần jeans basic."],
    "Phong cách hiện đại": ["Thử áo blazer cắt may tinh tế.", "Phối với giày loafers."]
}

def get_beauty_suggestion(skin_type, age_group, suggestion=None):
    skin_suggestion = beauty_suggestions.get(skin_type, ["Chăm sóc da cơ bản."])
    age_suggestion = beauty_suggestions.get(age_group, ["Trang điểm nhẹ nhàng."])
    result = skin_suggestion + age_suggestion
    
    if suggestion and suggestion in beauty_suggestions:
        result.extend(beauty_suggestions[suggestion])
    return result

def get_fashion_suggestion(color_type, style, suggestion=None):
    color_suggestion = fashion_suggestions.get(color_type, ["Phối màu trung tính."])
    style_suggestion = fashion_suggestions.get(style, ["Thử phong cách đơn giản."])
    result = color_suggestion + style_suggestion
    
    if suggestion and suggestion in fashion_suggestions:
        result.extend(fashion_suggestions[suggestion])
    return result