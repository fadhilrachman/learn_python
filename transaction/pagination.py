# blog/pagination.py
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5  # Jumlah item per halaman
    page_size_query_param = 'page_size'  # Dapat diubah oleh klien
    max_page_size = 100  # Ukuran maksimum yang dapat ditetapkan oleh klien
