import { useState } from "react";

export default function ImageUploader({ title }) {
  const [image, setImage] = useState(null);

  function handleChange(e) {
    const file = e.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
    }
  }

  return (
    <div className="card">
      <h2>{title}</h2>

      {image ? (
        <img
          src={image}
          alt="Preview"
          className="preview"
        />
      ) : (
        <div className="placeholder">
          No Image Selected
        </div>
      )}

      <input
        type="file"
        accept="image/*"
        onChange={handleChange}
      />
    </div>
  );
}
