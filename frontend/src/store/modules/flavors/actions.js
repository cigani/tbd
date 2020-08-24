import axios from "axios";
import {SET_FLAVORS, SET_SPECTRUM, SET_SPECTRUMS} from "@/store/modules/flavors/mutation-types";

export default {
  getFlavorsList(context) {
    return axios.get('/api/flavors')
      .then(response => {
        context.commit(SET_FLAVORS, response.data)
      })
      .catch(e => {
        console.log(e)
      })
  },
    getSpectrumList(context) {
    return axios.get('/api/spectrums')
      .then(response => {
        context.commit(SET_SPECTRUMS, response.data)
      })
      .catch(e => {
        console.log(e)
      })
  },
    getSpectrum(context, pk) {
    return axios.get('/api/spectrums/' + pk)
      .then(response => {
        context.commit(SET_SPECTRUM, response.data)
      })
      .catch(e => {
        console.log(e)
      })
  },
}
