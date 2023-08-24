// eslint-disable 
<template>
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
</template>

<script>
export default {
  data() {
    return {
      red: 0,
      green: 0,
      blue: 0,
    };
  },
  computed: {
    colorPreviewStyle() {
      return {
        backgroundColor:
          "rgb(" + this.red + ", " + this.green + ", " + this.blue + ")",
      };
    },
  },
  methods: {
    updateColor() {
      // Do something with the RGB values
    },
  },
};
</script>

<style scoped>
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
</style>
