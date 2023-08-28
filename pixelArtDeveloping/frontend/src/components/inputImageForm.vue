<template>
  <div class="block-editor">
    <div class="rgb-picker">
      <div class="color-preview" :style="colorPreviewStyle"></div>
      <div class="controls">
        <label for="red">Red:</label>
        <input
          id="red"
          type="number"
          min="0"
          max="255"
          v-model="red"
          @input="updateColor"
        />
      </div>
      <div class="controls">
        <label for="green">Green:</label>
        <input
          id="green"
          type="number"
          min="0"
          max="255"
          v-model="green"
          @input="updateColor"
        />
      </div>
      <div class="controls">
        <label for="blue">Blue:</label>
        <input
          id="blue"
          type="number"
          min="0"
          max="255"
          v-model="blue"
          @input="updateColor"
        />
      </div>
    </div>
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
      <button class="upload-form__button" @click="Submit" :style="colorPreviewStyle">Отправить</button>
      <div v-if="file" class="upload-form__preview">
        <img
          :src="previewUrl"
          :alt="file.name"
          class="upload-form__preview-image"
        />
      </div>
    </div>
    <div class="preview-image">
      <img :src="imageUrl" class="image">
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      file: null,
      red: 0,
      green: 0,
      blue: 0,
      previewUrl: null,
      imageUrl: "",
    };
  },
  computed: {
    colorPreviewStyle() {
      console.log(this.red, this.green, this.blue);
      return {
        backgroundColor:
          "rgb(" + this.red + ", " + this.green + ", " + this.blue + ")",
      };
    },
  },
  methods: {
    Submit() {
      this.submitImage();
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
      formData.append("r", this.red);
      formData.append("g", this.green);
      formData.append("b", this.blue);
      // Execute the AJAX request to the Django server for image processing
      axios
        .post("/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFToken": getCookie("csrftoken"),
          },
          responseType: 'blob', // Add this option to handle the binary data
        })
        .then((response) => {
          console.log(response);
          this.imageUrl = URL.createObjectURL(response.data)
        })
        .catch((error) => {
          console.error(error);
          alert("Произошла ошибка при загрузке изображения");
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
.block-editor{
  background-color: #fff;  
  width: 100%;
  height: 50vh;
  display: flex;
  margin-top:10%;
  margin-right: 5%;
}
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
  border-radius: 20px;
  border: none;
  color: #fff;
  text-align: center;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.upload-form__button:hover {
  background-color: hsl(276, 79%, 69%);
  box-shadow:
    1px 1px hsl(276, 79%, 69%),
    3px 3px #53ea93,
    5px 5px hsl(276, 79%, 69%),
    7px 7px #53ea93,
    9px 9px hsl(276, 79%, 69%);
  -webkit-transform: translateX(-7px);
  transform: translateX(-7px);
  -webkit-transition: all 0.3s ease;;
  -moz-transition: all 0.3s ease;;
  -o-transition: all 0.3s ease;;
  transition: all 0.3s ease;
}

.upload-form__preview {
  margin-top: 1rem;
}

.upload-form__preview-image {
  max-width: 100%;
  border-radius: 4px;
}

.rgb-picker {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.color-preview {
  width: 200px;
  height: 200px;
  margin-bottom: 1rem;
}
.color-preview:hover{
  -webkit-transition: all 0.3s ease;;
  -moz-transition: all 0.3s ease;;
  -o-transition: all 0.3s ease;;
  transition: all 0.3s ease;
}
.controls {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 1rem;
  align-items: center;
}

label {
  font-weight: bold;
}

input {
  width: 100%;
  padding: 0.5rem;
}
.preview-image {
  position: relative;
  max-width: 200px;
}

.image {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}
.image:hover{
  transform: scale(1.3) ;
  box-shadow:
    1px 1px hsl(276, 79%, 69%),
    3px 3px #53ea93,
    5px 5px hsl(276, 79%, 69%),
    7px 7px #53ea93,
    9px 9px hsl(276, 79%, 69%);
  -webkit-transform: translateX(-7px);
  transform: translateX(-7px);
  -webkit-transition: all 0.3s ease;;
  -moz-transition: all 0.3s ease;;
  -o-transition: all 0.3s ease;;
  transition: all 0.3s ease;
}
</style>