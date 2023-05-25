<template>
<div class="card" style="width: 18rem;">
  <ul data-role="listview" data-count-theme="b" data-inset="true">
    <li class="lili" style="font-size: 14pt">
      ({{ info.name }})<br>
      {{ info.openingPrice }} 
      <span :style="{ color: RiseFallColor, 'font-weight': 'bold' }">
        {{ info.change === 'RISE' ? '▲' : '▼' }} {{ info.changePrice.toFixed(2) }}
      </span>
    </li>
    <li class="lili" style="font-size: 12pt">
      살때 : {{ info.cashBuyingPrice.toFixed(2) }}<br>
      팔때 : {{ info.cashSellingPrice.toFixed(2) }}<br>
      보낼때 : 
      <span :style="{ color: RiseFallColor, 'font-weight': 'bold' }">
        {{ info.ttSellingPrice.toFixed(2) }}
      </span><br>
      받을때 : {{ info.ttBuyingPrice.toFixed(2) }}
    </li>
    <li class="lili" style="color:gray">Date: {{ info.date }}</li>
  </ul>
</div>

</template>

<script>
export default {
name: 'ChangeInfoCard',
props: {
    info: Object,
},
computed: {
    RiseFallColor() {
    return this.info.change === 'FALL' ? 'blue' : 'red';
    },
},
};
</script>

<style>
  .lili {
    list-style-type: none; /* 리스트 항목의 점 제거 */
    padding-left: 0; /* 왼쪽 여백 제거 */
  }
/* 추가적인 스타일링을 하시려면 여기에 작성하세요 */
</style>
  