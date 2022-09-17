<template>
  <v-app id="about" :style="{ background: '#FFB2A3' }">
    <v-container fluid>
      <v-card tile class="mx-5 mt-15" height="570px" color="#ffc2b4">
        <v-row>
          <v-col cols="12" md="6" class="mt-10 mb-10">
            <v-row class="justify-center">
              <img :src="require('@/assets/img/profile.png')" height="500" width="500" />
            </v-row>
          </v-col>
          <v-col cols="12" md="6" class="px-0 d-flex align-center">
            <v-row>
              <v-col cols="12" md="12" class="px-8 pt-5">
                <h1 class="white--text mt-8">ねおきもちもち</h1>
                <h2 class="white--text mt-3">快適な朝を過ごしませんか？</h2>
                <h4 class="white--text mt-5">
                  寝起きもちもちは朝人と話すことで快適な目覚めを届けるサービスです！<br />
                  毎朝違う人と話して脳を活性化させましょう！
                </h4>
              </v-col>
              <v-col cols="12" md="8"> </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card>

      <v-card tile class="mx-10 mt-5" color="#F4927E">
        <v-row>
          <v-col cols="12" md="12" class="px-8 pt-5">
            <h3 class="white--text mt-8">朝型になりたい理由</h3>
            <h4 class="white--text mt-3">
              起きてから頭が冴えず、二度寝をした経験は誰にでもあると思います<br />
              二度寝は寝坊の天敵です！<br />
              子供から大人まで、誰しも寝坊をしてしまうと人に迷惑をかけてしまう可能性があります<br />
              実際車掌さんが寝坊をしてしまって乗客を待たせた例もあるんです (参考リンク)<br />
              皆さんが二度寝をしたくないのであればこのサービスを使ってみてはいかがでしょうか？
            </h4>
            <v-btn rounded color="#EE7A63" dark target="_blank" href="https://www3.nhk.or.jp/lnews/aomori/20220624/6080016422.html" class="withoutupercase px-8 mt-10 0 white--text"> 参考リンク </v-btn>
          </v-col>
          <v-col cols="12" md="8"> </v-col>
        </v-row>
      </v-card>

      <v-card tile class="mx-10 mt-5" color="#F4927E">
        <v-row>
          <v-col cols="12" md="12" class="px-8 pt-5">
            <h3 class="white--text mt-8">話すと寝起きがよくなる！？</h3>
            <h4 class="white--text mt-3">
              アメリカの研究によると会話をするとガムをかんだり音楽を聴いたりするより<br />
              覚醒までの時間が2倍程度改善することがわかりました。<br />
              会話は効率的に人を覚醒させる手法です
            </h4>
            <v-btn rounded color="#EE7A63" dark target="_blank" href="https://www.researchgate.net/publication/266747357_Providing_Views_of_the_Driving_Scene_to_Drivers'_Conversation_Partners_Mitigates_Cell-Phone-Related_Distraction" class="withoutupercase px-8 mt-10 0 white--text"> 参考リンク </v-btn>
          </v-col>
          <v-col cols="12" md="8"> </v-col>
        </v-row>
      </v-card>

      <v-card tile class="mx-10 mt-5" color="#F4927E">
        <v-row>
          <v-col cols="12" md="12" class="px-8 pt-5">
            <h3 class="white--text mt-8">話すと寝起きがよくなる！？</h3>
            <h4 class="white--text mt-3">
              アメリカの研究によると会話をするとガムをかんだり音楽を聴いたりするより<br />
              覚醒までの時間が2倍程度改善することがわかりました。<br />
              会話は効率的に人を覚醒させる手法です
            </h4>
          </v-col>
          <v-col cols="12" md="8"> </v-col>
        </v-row>
      </v-card>
    </v-container>
  </v-app>
</template>

<script lang="ts">
export default {
  name: "TopView",

  components: {},
};
</script>
<style scoped>
.white--text {
  color: white;
  font-weight: bold;
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
