/* global $ */
$(document).ready(function() {
    var amount_type = 'amount'
    function set_item_name() {
        if($('input[name="t3"]:checked').val() === 'M') {
            $('#item_name').val("Friends Membership - Monthly Recurring Dues Payment");
        } else if ($('input[name="t3"]:checked').val() === 'Y') {
            $('#item_name').val("Friends Membership - Annual Recurring Dues Payment");
        }
    }
    function toggle_recurring() {
        $('#recurrence_interval').prop('hidden', !$('#is_recurring').prop("checked"));
        if ($('#is_recurring').prop("checked")) {
            $('#cmd').val('_xclick-subscriptions');
            amount_type = 'a3'
            set_item_name();
        } else {
            $('#cmd').val('_donations');
            $('#item_name').val("Friends Membership - Dues Payment");
            amount_type = 'amount'
        }
        set_amount();
    }
    function set_amount() {
        if ($('#dues_level').val() == 'other') {
            $('#other_amount_fg').prop('hidden', '');
            $('#other_amount').prop('name', amount_type);
            $('#dues_level').prop('name', '');
        } else {
            $('#other_amount_fg').prop('hidden', 'hidden');
            $('#other_amount').prop('name', '');
            $('#dues_level').prop('name', amount_type);
        }
    }
    $('#dues_level').change(set_amount);
    $('#is_recurring').change(toggle_recurring);
    $('input[name="t3"]').change(set_item_name);
    $('#is_recurring').prop("checked", false);
    toggle_recurring();
});
