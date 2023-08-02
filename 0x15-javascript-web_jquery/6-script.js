const $headerElem = $('header');
const $updateHeaderElem = $('div#update_header');

$updateheaderElem.on('click', () => {
	$headerElem.text('New Header!!!');
});
