<template>
	<table v-if="li.length !== 0">
		<tr>
			<th v-for="[key] of Object.entries(li[0])">
				{{ key }}
			</th>
		</tr>
		<tr v-for="i in li">
			<td v-for="[key, val] of Object.entries(i)">
				{{ val }}
			</td>
		</tr>
	</table>
</template>



<script>
export default {
	props: {
		li: {
			type: Array,
			reqiured: true
		}
	}
}
</script>



<style scoped>
table {
	margin: auto;
	width: 80vw;
	border: 1px solid grey;
}

th {
	padding: 5px;
	border: 1px solid grey;
}

td {
	padding: 5px;
	border: 1px solid grey;
}
</style>