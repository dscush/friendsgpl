/* global $ */
$(document).ready(function() {
    function calculate_paypal_fees(dues_amount, fee_only=true) {
        dues_amount = parseFloat(dues_amount) || 0;
        var fee = ((dues_amount + 0.3) / (1 - 0.022));
        if (fee_only) {
            fee -= dues_amount;
        }
        fee = fee * 100;
        fee = Math.ceil(fee);
        fee = fee / 100;
        return fee;
    }
    function set_total_and_fees (amount) {
        $('#paypal-fee').text('$' + calculate_paypal_fees(amount));
        if ($('#add_paypal_fee').prop('checked')) {
            $('#total').text('$' + calculate_paypal_fees(amount, false));
            $('#hidden-total').val(calculate_paypal_fees(amount, false));
        } else {
            $('#total').text('$' + (parseFloat(amount) || 0));
            $('#hidden-total').val(parseFloat(amount) || 0);
        }
    }
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
            $('#hidden-total').prop('name', 'a3');
            set_item_name();
        } else {
            $('#cmd').val('_donations');
            $('#item_name').val("Friends Membership - Dues Payment");
            $('#hidden-total').prop('name', 'amount');
        }
        set_amount();
    }
    function set_amount() {
        if ($('#dues_level').val() == 'other') {
            set_total_and_fees($('#other_amount').val());
            $('#other_amount_fg').prop('hidden', '');
            $('#other_amount').attr('required', true);
            $('#dues_level').prop('name', '');
            $('#other_amount').on('input', function () {
                set_total_and_fees($('#other_amount').val());
            });
        } else {
            set_total_and_fees($('#dues_level').val());
            $('#other_amount_fg').prop('hidden', 'hidden');
            $('#other_amount').attr('required', false);
            $('#other_amount').prop('name', '');
            $('#other_amount').off('input');
        }
    }
    $('#dues_level').change(set_amount);
    $('#add_paypal_fee').change(set_amount);
    $('#is_recurring').change(toggle_recurring);
    $('input[name="t3"]').change(set_item_name);
    $('#is_recurring').prop("checked", false);
    toggle_recurring();
});
