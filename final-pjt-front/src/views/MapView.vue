<template>
    <div class="box-container">
        <div class="box">
            <BankSearch/>
        </div>

    </div>
</template>

<script>
import BankSearch from '@/components/BankSearch.vue'

export default {
name: 'MapView',
components: {
    BankSearch
}
}
</script>


<style>
  .box-container {
    display: flex;
    justify-content: center;
  }
  .box {
    width: 800px;
    width:800px;
    border: 1px solid black;
  }
</style>