<template>
  <div class="upload-form">
    <label class="upload-form__label" for="fileInput">
      <span class="upload-form__label-text">Выберите изображение</span>
      <input
        id="fileInput"
        type="file"
        ref="fileInput"
        @change="handleFileUpload"
      />
    </label>
    <button class="upload-form__button" @click="Submit">Отправить</button>
    <div v-if="file" class="upload-form__preview">
      <img
        :src="previewUrl"
        :alt="file.name"
        class="upload-form__preview-image"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      file: null,
      red:0,
      green:0,
      blue:0,
      previewUrl: null,
    };
  },
  methods: {
    Submit(){
      this.submitImage()
      this.submitRGB()
    },
    handleFileUpload() {
      this.file = this.$refs.fileInput.files[0];
      this.previewUrl = URL.createObjectURL(this.file);
    },
    submitImage() {
      if (!this.file) {
        console.log("Please select an image first.");
        return;
      }

      const formData = new FormData();
      formData.append("image", this.file);

      // Execute the AJAX request to the Django server for image processing
      axios
        .post("/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFToken": getCookie("csrftoken"),
          },
        })
        .then((response) => {
          console.log(response.data);
          // Handle the successful response
        })
        .catch((error) => {
          console.log(error);
          // Handle the error
        });
    },
    submitRGB() {
      const data = {
        red: document.getElementById("red").value,
        green: document.getElementById("green").value,
        blue: document.getElementById("blue").value,
      };

      const headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      };

      axios
        .post("/submit-rgb", data, { headers })
        .then((response) => {
          console.log(response.data);
          // Handle the successful RGB submission response
        })
        .catch((error) => {
          console.log(error);
          // Handle the error
        });
    },
  },
};

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
</script>
<style scoped>
.upload-form {
  width: 400px;
  margin: 0 auto;
}

.upload-form__label {
  display: block;
  margin-bottom: 1rem;
  border: 2px dashed #aaa;
  padding: 1rem;
  text-align: center;
  cursor: pointer;
}

.upload-form__label-text {
  display: block;
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 0.5rem;
}

.upload-form__button {
  display: block;
  width: 100%;
  padding: 0.75rem 1rem;
  background-color: #007bff;
  border: none;
  color: #fff;
  text-align: center;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.upload-form__button:hover {
  background-color: #0056b3;
}

.upload-form__preview {
  margin-top: 1rem;
}

.upload-form__preview-image {
  max-width: 100%;
  border-radius: 4px;
}
</style>
