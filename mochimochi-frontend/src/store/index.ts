import { createStore } from "vuex";
import axios from "axios";

type User = {
  token: string;
  name: string;
};

type State = {
  user: User | null;
};

export default createStore<State>({
  state: {
    user: null,
  },
  getters: {
    isLogin(state): boolean {
      return state.user !== null;
    },
    token(state): string | null {
      return state.user === null ? null : state.user.token;
    },
    name(state): string | null {
      return state.user === null ? null : state.user.name;
    },
  },
  mutations: {
    setUser(state, payload: User) {
      state.user = payload;
    },
  },
  actions: {
    // 現在のトークンでログインできてるかを返すAPIがあったら使いたい
    async fetchUser({ commit }) {
      // const data: User | null = { token: "aaaa", name: "iiii" };
      const data: User | null = null;
      commit("setUser", data);
    },
  },
  modules: {},
});
