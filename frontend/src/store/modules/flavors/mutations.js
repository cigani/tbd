import {SET_FLAVOR, SET_SPECTRUM, SET_FLAVORS, SET_SPECTRUMS} from "@/store/modules/flavors/mutation-types";

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
  [SET_SPECTRUM](state, {data}) {
    state.spectrum = data;
    state.meta = data.meta
  },
};
