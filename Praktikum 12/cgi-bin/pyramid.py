from math import sqrt

base_width = 10
height = 12

def calculate_area(width, height):
    base_w = float(width)
    height = float(height)
    tr_height = sqrt(((base_w/2)**2) + (height**2))
    area = (base_w**2) + (4 * (0.5 * base_w * tr_height))
    return area

print(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Luas Piramida</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
    <h1>Bangun Geometri</h1>
    <table>
        <tr>
            <td>Nama bangun</td>
            <td>:</td>
            <td>Piramida</td>
        </tr>
        <tr>
            <td>Dimensi (2D/3D)</td>
            <td>:</td>
            <td>3D</td>
        </tr>
        <tr>
            <td>Rumus luas</td>
            <td>:</td>
            <td>Luas alas + Jumlah luas sisi tegak</td>
        </tr>
        <tr>
            <td>Panjang alas</td>
            <td>:</td>
            <td>{base_width} m</td>
        </tr>
        <tr>
            <td>Tinggi bangun</td>
            <td>:</td>
            <td>{height} m</td>
        </tr>
        <tr>
            <td>Luas</td>
            <td>:</td>
            <td>{calculate_area(base_width, height)} m<sup>2<sup/></td>
        </tr>
    </table>
</body>
</html>
""")