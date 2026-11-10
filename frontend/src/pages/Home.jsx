import ImageUploader from "../components/ImageUploader";

export default function Home() {
  return (
    <div className="container">
      <h1>AI FaceSwap Studio</h1>
      <p>Upload two images and swap faces with AI</p>

      <div className="cards">
        <ImageUploader title="Source Face" />
        <ImageUploader title="Target Image" />
      </div>

      <button className="swap-btn">
        🔄 Swap Faces
      </button>
    </div>
  );
}
