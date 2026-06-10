const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

async function setupCamera() {
  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  video.srcObject = stream;
  return new Promise((resolve) => {
    video.onloadedmetadata = () => resolve(video);
  });
}

async function detectObjects() {
  const model = await cocoSsd.load();

  async function frame() {
    const predictions = await model.detect(video);

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw predictions
    predictions.forEach((p) => {
      ctx.strokeStyle = "red";
      ctx.lineWidth = 2;
      ctx.strokeRect(p.bbox[0], p.bbox[1], p.bbox[2], p.bbox[3]);
      ctx.fillStyle = "red";
      ctx.fillText(
        `${p.class} (${Math.round(p.score * 100)}%)`,
        p.bbox[0],
        p.bbox[1] > 10 ? p.bbox[1] - 5 : 10,
      );
    });

    requestAnimationFrame(frame);
  }
  frame();
}

setupCamera().then(detectObjects);
