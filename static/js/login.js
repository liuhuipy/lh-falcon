function topRightLogin() {
    login_popup()
}

function detect_ie() {
    var e = window.navigator.userAgent, t = e.indexOf("MSIE "), n = e.indexOf("Trident/");
    if (t > 0) return parseInt(e.substring(t + 5, e.indexOf(".", t)), 10);
    if (n > 0) {
        var a = e.indexOf("rv:");
        return parseInt(e.substring(a + 3, e.indexOf(".", a)), 10)
    }
    return !1
}

function find_password_form_submit() {
    $.ajax({
        cache: !1,
        type: "POST",
        url: "/user/password/find/",
        data: {
            account: $("#id_account").val(),
            geetest_challenge: $("#find_password_form .geetest_challenge").attr("value"),
            geetest_validate: $("#find_password_form .geetest_validate").attr("value"),
            geetest_seccode: $("#find_password_form .geetest_seccode").attr("value")
        },
        async: !0,
        beforeSend: function () {
            $("#findpassword_btn").html("提交中..."), $("#findpassword_btn").attr("disabled", "disabled")
        },
        success: function (e) {
            e.account ? $("#findpassword-tips").html(e.account).show(500) : e.captcha ? $("#findpassword-tips").html(e.captcha).show(500) : e.email_ue ? $("#findpassword-tips").html(e.email_ue).show(500) : e.mobile ? $("#findpassword-tips").html(e.mobile).show(500) : $("#id_account").val().indexOf("@") > 0 ? $("#findpassword-tips").html("找回密码邮件已发送").show(500) : ("failure" == e.status ? $("#mobile_code_password_form_message").html("手机短信验证码发送失败！") : ($("#mobile_code_password_form_message").html("手机短信验证码已发送，请查收！"), show_send_sms(60)), $("#id_mobile_f").val($("#id_account").val()), $("#forgetpswModal").modal("hide"), $("#forgetpswMobileModal").modal("show"))
        },
        complete: function () {
            $("#findpassword_btn").html("提交"), $("#findpassword_btn").removeAttr("disabled")
        }
    })
}

var init = function () {
    $(".zy_close").on({
        click: function () {
            $(this).parent().parent().parent().parent().parent().modal("hide")
        }
    }), login_popupvar && login_popup(), $("#login_form").keydown(function (e) {
        13 == e.keyCode && login_form_submit("login-form-tips")
    }), $("#find_password_form").keydown(function (e) {
        13 == e.keyCode && find_password_form_submit()
    }), $("#findpassword_btn").click(find_password_form_submit), $("#login_close").click(function () {
        var e = document.location.pathname;
        if (0 == e.search(/^\/lps-\w+?\/$/)) {
            var t = e.substring(5, e.length - 1);
            return maizi_trace.trace({
                suid: get_cookie("maiziuid"),
                action_id: "trace_lps4_login_cancel",
                trace_career_name: maizi_trace.career_name()
            }), console.log("lps4 pathname traced. career_name: " + t), !0
        }
    })
};
init();
console.log("\u002f\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u000d\u000a\u0020\u002a\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u002a\u0009\u0009\u000d\u000a\u0020\u002a\u0020\u0009\u0009\u0009\u0009\u0009\u0009\u0020\u0020\u0020\u0020\u0020\u0020\u4ee3\u7801\u5e93\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u002a\u000d\u000a\u0020\u002a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0077\u0077\u0077\u002e\u0064\u006d\u0061\u006b\u0075\u002e\u0063\u006f\u006d\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u002a\u000d\u000a\u0020\u002a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0009\u0009\u0020\u0020\u52aa\u529b\u521b\u5efa\u5b8c\u5584\u3001\u6301\u7eed\u66f4\u65b0\u63d2\u4ef6\u4ee5\u53ca\u6a21\u677f\u0009\u0009\u0009\u002a\u000d\u000a\u0020\u002a\u0020\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u0009\u002a\u000d\u000a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002f");