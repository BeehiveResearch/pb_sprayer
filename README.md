# pb_sprayer

Package ini berfungsi untuk menyalakan dan mematikan sprayer menggunakan Jetson GPIO.

Pin yang digunakan adalah GPIO9 (BCM), urutan nomor 7 pada board.

## Cara Menggunakan

Jalankan command:
```bash
ros2 run pb_sprayer sprayer_node
```

### Interface

| Service Name | Interface | Use |
| --- | --- | --- |
| `spray` | SetBool | `ros2 service call spray std_srvs/srv/SetBool "{data: True"}`

Berikan data `True` untuk menghidupkan spray dan `False` untuk mematikan.