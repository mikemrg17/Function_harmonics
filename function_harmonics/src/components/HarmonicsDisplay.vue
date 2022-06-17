<template>
  <div>
    <h3>Harmonics...</h3>
    <div v-if="0>1">
      <SignalDisplayer />
    </div>
  </div>
</template>

<script>
import SignalDisplayer from './SignalDisplayer.vue'

export default {
    name: 'HarmonicsDisplay',
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

    }
}
</script>

<style>

</style>