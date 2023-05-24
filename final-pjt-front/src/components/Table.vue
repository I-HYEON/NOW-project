<template>
  <tr>
    <th scope="row">{{table.intr_rate_type_nm}}</th>
    <td>{{table.save_trm}}개월</td>
    <td>저축 금리 : {{table.intr_rate}}%</td>
    <td>최고 우대금리 : {{table.intr_rate2}}%</td>
  </tr>
</template>

<script>
export default {
name: 'Table',
props: {
  table: Object
},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
      