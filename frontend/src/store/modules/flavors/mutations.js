import {
  SET_FLAVOR,
  SET_SPECTRUM,
  SET_FLAVORS,
  SET_SPECTRUMS,
  SET_ADDITIVES, SET_SUBSTRATES, SET_QMIDS
} from "@/store/modules/flavors/mutation-types";

export default {
  /**
   *
   * @param { object } state
   * @param data
   */
  [SET_FLAVORS](state, data) {
    state.flavors = data;
  },
  [SET_SPECTRUMS](state, data) {
    state.spectrums = data
  },
  [SET_FLAVOR](state, {data}) {
    state.flavor = data;
  },
  [SET_SPECTRUM](state, data) {
    state.spectrum = data.data;
    state.meta = data.meta
  },
  [SET_ADDITIVES](state, data){
    state.additives = data
  },
  [SET_SUBSTRATES](state, data){
    state.substrates = data
  },
  [SET_QMIDS](state, data){
    state.qmids = data
  }
};
