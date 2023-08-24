/* eslint-disable */
import { createApp } from "vue";
import App from "./components/inputImageForm.vue";
import "./registerServiceWorker";
import RGBPicker from "./components/RGBPicker.vue";
createApp(App).mount("#app");
createApp(RGBPicker).mount("#rgb");
/*
// eslint-disable 
import { createApp } from "vue";
import App from "../../frontend/src/components/inputImageForm.vue";
import "../../frontend/src/registerServiceWorker";
import RGBPicker from "../../frontend/src/components/RGBPicker.vue";
createApp(App).mount("#app");
createApp(RGBPicker).mount("#rgb");
*/