import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Animal Hospital Roblox 2.5D", layout="centered")

st.title("Animal Hospital - Roblox 2.5D")
st.write("Game quan ly benh vien thu cung 2.5D (Roblox Inspired)")

game_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; margin: 0; }
        canvas { background: #1e293b; border: 2px solid #475569; display: block; margin: 0 auto; }
        #ui { margin-top: 10px; font-size: 14px; color: #38bdf8; }
    </style>
</head>
<body>
    <canvas id="game" width="700" height="400"></canvas>
    <div id="ui">DI CHUYEN: DUNG PHIM MUI TEN HOAC WASD | BIKENH VIEN THU CUNG 2.5D</div>
    <script>
        const canvas = document.getElementById('game');
        const ctx = canvas.getContext('2d');
        const TILE_W = 60, TILE_H = 30, MAP_SIZE = 8;
        const ORIGIN_X = canvas.width / 2, ORIGIN_Y = 60;

        function iso(gx, gy) {
            return { x: ORIGIN_X + (gx - gy) * (TILE_W / 2), y: ORIGIN_Y + (gx + gy) * (TILE_H / 2) };
        }

        function drawTile(gx, gy, cTop, height = 0) {
            const p = iso(gx, gy);
            const topY = p.y - height;
            ctx.beginPath();
            ctx.moveTo(p.x, topY);
            ctx.lineTo(p.x + TILE_W / 2, topY + TILE_H / 2);
            ctx.lineTo(p.x, topY + TILE_H);
            ctx.lineTo(p.x - TILE_W / 2, topY + TILE_H / 2);
            ctx.closePath();
            ctx.fillStyle = cTop;
            ctx.fill();
            ctx.strokeStyle = '#0f172a';
            ctx.stroke();
        }

        let px = 1, py = 1;
        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowUp' || e.key === 'w') py = Math.max(0, py - 0.5);
            if (e.key === 'ArrowDown' || e.key === 's') py = Math.min(MAP_SIZE - 1, py + 0.5);
            if (e.key === 'ArrowLeft' || e.key === 'a') px = Math.max(0, px - 0.5);
            if (e.key === 'ArrowRight' || e.key === 'd') px = Math.min(MAP_SIZE - 1, px + 0.5);
        });

        function render() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let x = 0; x < MAP_SIZE; x++) {
                for (let y = 0; y < MAP_SIZE; y++) {
                    drawTile(x, y, (x + y) % 2 === 0 ? '#334155' : '#1e293b');
                }
            }
            drawTile(3, 3, '#e11d48', 12); // Bed / Anomaly
            
            // Player
            const pos = iso(px, py);
            ctx.fillStyle = '#38bdf8';
            ctx.fillRect(pos.x - 6, pos.y - 20, 12, 16);
            ctx.fillStyle = '#fde047';
            ctx.beginPath();
            ctx.arc(pos.x, pos.y - 24, 5, 0, Math.PI * 2);
            ctx.fill();

            requestAnimationFrame(render);
        }
        render();
    </script>
</body>
</html>
"""

components.html(game_code, height=480)
