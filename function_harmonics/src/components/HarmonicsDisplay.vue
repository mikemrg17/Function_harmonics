<template>
  <div>
    <h3>Harmonics...</h3>
    {{fourier_serie}}
    <div v-if="displayHarmonic == 1">
      <div v-for="(harmonic, index) in fourier_serie" :key="index">
        <SignalDisplayer :harmonic="harmonic" :nHarmonic="index"/>
      </div>
    </div>
  </div>
</template>

<script>
import SignalDisplayer from './SignalDisplayer.vue'

export default {
    name: 'HarmonicsDisplay',
    data(){
      return {
        displayHarmonic: 0
      }
    },
    components:{
      SignalDisplayer
    },
    props:{
      fourier_serie:{
        type: Array,
        default: () => []
      }
    },
    mounted(){
      this.displayHarmonic = 1
    }
}
</script>

<style>

</style>