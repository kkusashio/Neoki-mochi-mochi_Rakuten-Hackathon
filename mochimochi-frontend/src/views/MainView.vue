<script lang="ts" setup>
import axios from "axios";
import { reactive, ref } from "vue";
import store from "../store/index";

const time = ref("7:00");
const date = ref("");
const zoom = reactive({ url: "", date: "" });
const responseNotice = ref("");

const setZoomUrl = async () => {
  const requestDate = new Date('2022-09-17T06:50');
  requestDate.setHours(requestDate.getHours() + 9);
  await axios
    .get("/meetings/", {
      params: {
        date: requestDate.toISOString(),
      },
      headers: {
        Authorization: "Token " + store.getters.token,
      },
    })
    .then((e) => {
      if (!e.data.proccessed) return;
      zoom.url = e.data.zoom_url;
      zoom.date = e.data.date;
      console.log(zoom);
    })
    .catch((e) => console.error(e));
};

const settingAlarm = async () => {
  const dateObject = new Date(date.value);
  const [hour, min] = time.value.split(":").map((e) => Number(e));
  dateObject.setHours(hour + 9, min, 0, 0);
  const dateString = dateObject.toISOString();

  await axios
    .post(
      "/register/",
      { date: dateString },
      {
        headers: {
          Authorization: "Token " + store.getters.token,
        },
      }
    )
    .then((e) => {
      console.log(e);
      setResponseNotice("登録に成功しました");
    })
    .catch((e) => {
      console.error(e);
      setResponseNotice("登録に失敗しました");
    });
};

const setResponseNotice = (message: string) => {
  responseNotice.value = message;
  setTimeout(() => (responseNotice.value = ""), 2000);
};

const jumpZoom = () => {
  axios.post(
    "/participate/",
    { date: zoom.date },
    {
      headers: {
        Authorization: "Token " + store.getters.token,
      },
    }
  );
};

//created
setZoomUrl();
date.value = new Date()
  .toLocaleDateString("ja-JP", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  })
  .split("/")
  .join("-");
</script>

<template>
  <v-app id="about" :style="{ background: '#FFF' }">
    <v-container fluid>
      <v-card class="mx-10 mt-5" color="#F4927E">
        <v-row class="mb-3">
          <v-col cols="12" md="12" class="pl-8 pt-5">
            <h3 class="white--text mt-8">{{ store.getters.name }}さんようこそ</h3>
          </v-col>
        </v-row>
        <div>
          <router-link to="user" class="link-button">
            <v-btn rounded color="#EE7A63" dark class="withoutupercase px-8 mb-10 white--text"> ユーザーページへ移動 </v-btn>
          </router-link>
        </div>
      </v-card>

      <v-card class="mx-10 mt-5" color="#F4927E">
        <v-row>
          <v-col cols="12" md="12" class="pl-8 pt-5">
            <h3 class="white--text mt-8 mb-3">起きる時間を設定してください</h3>
            <input type="date" v-model="date" />
            <select name="" id="" v-model="time">
              <option value="7:00">7:00</option>
              <option value="7:15">7:15</option>
              <option value="7:30">7:30</option>
              <option value="7:45">7:45</option>
              <option value="8:00">8:00</option>
              <option value="8:15">8:15</option>
              <option value="8:30">8:30</option>
              <option value="8:45">8:45</option>
              <option value="9:00">9:00</option>
              <option value="9:15">9:15</option>
              <option value="9:30">9:30</option>
              <option value="9:45">9:45</option>
              <option value="10:00">10:00</option>
            </select>
          </v-col>
        </v-row>
        <v-row class="message-box">
          <v-col class="message-box__text">
            {{ responseNotice }}
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn rounded color="#EE7A63" dark class="withoutupercase px-8 mt-2 mb-10 white--text link-button" @click="settingAlarm"> 追加 </v-btn>
          </v-col>
        </v-row>
      </v-card>

      <v-card class="mx-10 mt-5" color="#F4927E">
        <v-row>
          <v-col cols="12" md="6" class="mt-5 mb-5">
            <v-card tile class="mx-10 mt-5 py-5" color="#DE572C">
              <v-icon color="#FFF" size="33" class="ml-3"> mdi-card-account-phone-outline </v-icon>
              <h3 class="white--text ml-3 mt-4">Move to Zoom link</h3>
              <p class="white--text ml-3 mt-6">時間になったらzoomに移動しましょう!<br /></p>
              <v-btn v-if="zoom.url !== ''" color="#EE7A63" class="mt-3 white--text" target="_blank" :href="zoom.url" @click="jumpZoom">
                リンクに移動
                <v-icon right>mdi-arrow-right</v-icon>
              </v-btn>
              <v-btn color="#EE7A63" class="mt-3 white--text" v-else>まだ時間になっていません</v-btn>
            </v-card>
          </v-col>
          <v-col cols="12" md="6" class="mt-5 mb-5">
            <v-card tile class="mx-10 mt-5 py-5" color="#DE572C">
              <v-icon color="#FFF" size="33" class="ml-3">mdi-view-list-outline</v-icon>
              <h3 class="white--text ml-3 mt-4">参加後アンケート</h3>
              <p class="white--text ml-3 mt-6">もちもちを終えたらアンケートに答えよう！<br /></p>
              <v-btn color="#EE7A63" class="mt-3 white--text">
                アンケート記入
                <v-icon right>mdi-arrow-right</v-icon>
              </v-btn>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </v-app>
</template>

<style scoped lang="scss">
.link-button {
  text-decoration: none;
  color: white;
}

.white--text {
  color: white;
  font-weight: bold;
}

.message-box {
  height: 40px;
  &__text {
    font-size: 20px;
  }
}
.top {
  margin-top: 180px;
}

.topInverse {
  margin-top: -250px;
}

.topTolbar {
  margin-top: 100px;
  text-align: center;
}

.first {
  width: 100%;
  height: 610px;
  background: linear-gradient(to right, #181818, #181818 50%, #181818 50%, #111111 50%);
  text-align: center;
  padding: 2rem 2rem;
}

.second {
  width: 100%;
  height: 400px;
  background: #181818;
  text-align: center;
  padding: 2rem, 2rem;
}

.secondchild1 {
  display: inline-block;
  background-color: #1e1e1e;
  padding: 2rem, 2rem;
  vertical-align: middle;
  text-align: left;
  margin-top: 250px;
}

.child {
  display: inline-block;
  padding: 2rem 1rem;
  vertical-align: middle;
  text-align: left;
  margin-right: 8px;
}

.bgColor1 {
  background-color: #1e1e1e;
}

.bgColor2 {
  background-color: #ce1d2e;
}

.child1 {
  display: inline-block;
  padding: 2rem 1rem;
}

.child2 {
  display: inline-block;
  width: 245px;
  vertical-align: middle;
}

.mRight {
  margin-right: 8px;
}

.mButton {
  margin-right: 8px;
}

.padding {
  padding: 8px 0px;
}

.col-12.padd {
  padding: 12px 0 !important;
}

.col-12.childcol {
  padding: 0 !important;
}

h1.number {
  font-size: 50px;
  font-weight: bold;
}
</style>
