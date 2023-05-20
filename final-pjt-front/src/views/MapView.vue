<template>
    <div>
        <h1>가까운 은행검색</h1>
        <BankSearch/>
    </div>
</template>

<script>
import BankSearch from '@/components/BankSearch.vue'

export default {
name: 'MapView',
components: {
    BankSearch
},
}
</script>


<style>

</style>