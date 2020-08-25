import axios from "axios";
import {
  SET_FLAVORS,
  SET_SPECTRUM,
  SET_SPECTRUMS,
  SET_ADDITIVES,
  SET_SUBSTRATES
} from "@/store/modules/flavors/mutation-types";

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
  getSubstrates(context) {
    return axios.get('/api/flavors/substrates')
      .then(response => {
        let substrates = []
        for (const i in response.data){
          substrates.push(response.data[i].substrate)
        }
        context.commit(SET_SUBSTRATES, substrates)
      })
      .catch(e => {
        console.log(e)
      })
  },
  getAdditives(context) {
    return axios.get('/api/flavors/additives')
      .then(response => {
        let additives = []
        for (const i in response.data){
          additives.push(response.data[i].additive)
        }
        context.commit(SET_ADDITIVES, additives)
      })
      .catch(e => {
        console.log(e)
      })
  },

}