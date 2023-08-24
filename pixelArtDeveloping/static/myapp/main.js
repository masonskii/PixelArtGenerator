import { createApp } from "vue";
import App from "../../frontend/src/components/inputImageForm.vue";
import "../../frontend/src/registerServiceWorker";
import RGBPicker from "../../frontend/src/components/RGBPicker.vue";
createApp(App).mount("#app");
createApp(RGBPicker).mount("#rgb");