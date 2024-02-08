# 1. Tạo một movies list chứa tên các bộ phim đã xem

movies_list = ["trảng quỳnh","Naruto","Fairy Tail","gió","Fairy Tail"]
# 2. Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
movies = input("nhập vào một bộ phim khác không có trong movies list: ")

# 3. Thêm bộ phim vừa nhập vào cuối của danh sách movies
movies_list.append(movies)
print(f"danh sách sau khi thay đổi là: {movies_list}")

# 4. In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
print(f"Bộ phim đầu tiên {movies_list[0]}")
print(f"Bộ phim cuối cùng {movies_list[-1]}")
print(f"Bộ phim ở giữa {movies_list[len(movies_list)//2]}")

# 5. Tính tổng bộ phim có trong movies
print(f"tổng bộ phim có trong movies: {len(movies_list)}")

# 6. Xóa bộ phim đầu và cuối trong movies
del movies_list[0]
del movies_list[-1]
print(f"danh sách movies sau khi thêm là {movies_list}")

# 7. Lấy ra và xóa bộ phim cuối cùng trong movies
movies_ = movies_list.pop()
print(f"Bộ phim cuối cùng: {movies_}")
print(f"danh sách movies hiện tại là: {movies_list}")

# 8. Chèn một bộ phim bất kỳ vào đầu danh sách movies
movies_list.insert(1,"One Piece")
print(movies_list)

# 9. Đếm số bộ phim có tiêu đề là "One Piece"
count = movies_list.count("One Piece")
print(f"số bộ phim có tiêu đề là One Piece là: {count}")

# 10. Tìm vị trí của bộ phim có tên là "gió"
print(f'vị trí của bộ phim có tên là "gió" là {movies_list.index("gió")}')

# 11. Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
new_movies = ["Pokemon","Bleach"]
movies_list.extend(new_movies)
print(f"danh sách sau khi thêm là: {movies_list}")

# 12. Xóa tất cả các bộ phim có trong danh sách
movies_list.clear()
print(f"danh sách sau khi xóa là: {movies_list}")