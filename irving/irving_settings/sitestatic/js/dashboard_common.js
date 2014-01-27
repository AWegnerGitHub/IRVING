/**************************************************************************************
 * Common functions for the dashboard application
 *
 * 
 *
 *
 **************************************************************************************/

function dashboardSelector() {
// Shows the dashboard menu for current logged in user
    var c = document.getElementById("dashMenu");
    var a = document.getElementById("dashMenuButton");
    var b = a.innerHTML;
    if (c.style.display == "none" || c.style.display == "") {
        c.style.display = "block";
        a.className = "current";
        a.innerHTML = '<li id="dashMenuButton"><a onclick="dashboardSelector()" href="javascript:void(0)">Dashboards</a></li>';
    } else {
        c.style.display = "none";
        a.className = "";
        a.innerHTML = b
    }
}

function pollingIntervalInfo() {/* Empty Function; Stub for the Interval button in the footer */}
function pollingUpdateInfo() {/* Empty Function; Stub for the last run time button in the footer */}

function subReturn(a) {
// Close the menu
    var b = document.getElementById(a);
    b.style.display = "none";
    b = document.getElementById("dashMenuView");
    b.style.display = "block"
}

function runQueries() {
// The heart of the dashboard. This function executes each query, waits for results and displays them back to the board

		// First the main dashboard
	$('span[id*=dashquery_ugq_]:visible').each(function() {
		chld = $('#'+this.id).children(".dashquery_result");
		resultspan = chld.attr('id');
		jQuery('#'+resultspan).removeClass('loading-indicator-square');
		jQuery('#'+resultspan).removeClass('query_fatal');
		jQuery('#'+resultspan).removeClass('query_warning');
		jQuery('#'+resultspan).removeClass('query-error');
		jQuery('#'+resultspan).html("&nbsp;");
		jQuery('#'+resultspan).addClass('loading-indicator-square');
		
		$.ajax({
			type: "GET",
			dataType: "json",
			data: {ugq_id : this.id, res_span: resultspan},	
			url: "/xhr/runquery/",
			//error: function(xhr, statusText) { alert("Error: "+statusText); },
			success: function(msg){ 
				if (msg.success == true) {
						jQuery('#'+msg.res_span).removeClass('loading-indicator-square');
						jQuery('#'+msg.res_span).html(msg.resultsetcount);
						
						if ((parseInt(msg.warning_threshold, 10) != 0) || (parseInt(msg.fatal_threshold,10) != 0)) {
							if ((parseInt(msg.warning_threshold, 10) != 0) && (parseInt(msg.fatal_threshold,10) != 0)) {
								if ((parseInt(msg.resultsetcmp, 10) >= parseInt(msg.warning_threshold,10)) && (parseInt(msg.resultsetcmp,10) < parseInt(msg.fatal_threshold,10))) {
									jQuery('#'+msg.res_span).addClass('query_warning');
								}
							}
							if ((parseInt(msg.resultsetcmp, 10) >= parseInt(msg.fatal_threshold,10))) {
								jQuery('#'+msg.res_span).addClass('query_fatal');
							}
						}
					}
				else {
					jQuery('#'+msg.res_span).html('&nbsp;');
					jQuery('#'+msg.res_span).removeClass('loading-indicator-square');
					jQuery('#'+msg.res_span).addClass('query-error');			
					}
				}
			}
		);
	});
		
		// Now the error panel
	$('span[id*=dashquery_err_]:visible').each(function() {
		chld = $('#'+this.id).children(".dashquery_result");
		resultspan = chld.attr('id');
		jQuery('#'+resultspan).removeClass('loading-indicator-square');
		jQuery('#'+resultspan).removeClass('query_fatal');
		jQuery('#'+resultspan).removeClass('query_warning');
		jQuery('#'+resultspan).removeClass('query-error');
		jQuery('#'+resultspan).html("&nbsp;");
		jQuery('#'+resultspan).addClass('loading-indicator-square');
		
		$.ajax({
			type: "GET",
			dataType: "json",
			data: {qry_id : this.id, res_span: resultspan},	
			url: "/xhr/runquery/",
			//error: function(xhr, statusText) { alert("Error: "+statusText); },
			success: function(msg){ 
				if (msg.success == true) {
					jQuery('#'+msg.res_span).html(msg.resultsetcount);
					if ((parseInt(msg.warning_threshold, 10) != 0) || (parseInt(msg.fatal_threshold,10) != 0)) {
						if ((parseInt(msg.resultsetcmp, 10) >= parseInt(msg.fatal_threshold,10))) {
							jQuery('#'+msg.res_span).addClass('query_fatal');
						}
					}
					jQuery('#'+msg.res_span).removeClass('loading-indicator-square');
					}
				else {
					jQuery('#'+msg.res_span).html('&nbsp;');
					jQuery('#'+msg.res_span).removeClass('loading-indicator-square');
					jQuery('#'+msg.res_span).addClass('query-error');			
					}
				}
			}
		);
	});
}

function positionFooter() {
// Align the footer properly
	$(window).bind("load", function() {     
		var footerHeight = 0,
		footerTop = 0,
		$footer = $("#footContainer");
		positionFooter();
      
		function positionFooter() {
			footerHeight = $footer.height();
            footerTop = ($(window).scrollTop()+$(window).height()-footerHeight-20)+"px";
			if ( ($(document.body).height()+footerHeight) < $(window).height()) {
				$footer.css({
					position: "absolute",
					top: footerTop
					})
			} 
			else {
				$footer.css({
					position: "static"
					})
			}
		}
		$(window)
			.scroll(positionFooter)
            .resize(positionFooter)
		});
}

function startPolling(toggle) {
// Start the cycle to poll at a set interval. This interval is calculated in milliseconds (which is why we multiple by 60,000)
	$pollingInterval = $("#pollintval").text();
	if (toggle == true)
	{
		poll();
		$.doTimeout('refresh_loop', $pollingInterval * 60000, function()
		{
			poll();	
			return true;
		});
	}
	else
	{
		$.doTimeout('refresh_loop');
		var cssObj = {
			'background' : '#BDE5F8',
			'color' : '#000'
		}
		$("#pollingstatus").html('<a onclick="startPolling(true)" href="javascript:void(0)">Paused...</a>');
		$("html > body > div#footContainer > div#footer > ul > li#pollingstatus > a").css(cssObj);
	}
}

function poll() {
// Force poll action to occur
	runQueries();
	var now = new Date();
	$("#pollupdstamp").html(now.format("mmm d, yyyy 'at' h:MM tt"));
	$("#pollingstatus").html('<a onclick="startPolling(false)" href="javascript:void(0)">Running</a>')
}

function clearAllOverlays() {
// Clear the over lay icons (loading image, error image, etc)
	$('span[id*=dashquery_ugq_]:visible').each(function() {
		chld = $('#'+this.id).children(".dashquery_result");
		resultspan = chld.attr('id');
		jQuery('#'+resultspan).removeClass('loading-indicator-square');
		jQuery('#'+resultspan).removeClass('query-error');
	});
	
	$('span[id*=dashquery_err_]:visible').each(function() {
		chld = $('#'+this.id).children(".dashquery_result");
		resultspan = chld.attr('id');
		jQuery('#'+resultspan).removeClass('loading-indicator-square');
		jQuery('#'+resultspan).removeClass('query-error');
	});
}

function saveGroupOrder(dashOrder){
// Save the order of realigned dashboard groups
	$.ajax({
		type: "GET",
		dataType: "json",
		data: {currentOrder: dashOrder},	
		url: "/xhr/boardorder",
		//error: function(xhr, statusText) { alert("Error: "+statusText); },
		success: function(msg){ 
			/* Don't do anything */
			}
		}
	);
}

function saveQueryOrder(qOrder){
// Save the order of realigned dashboard groups
	$.ajax({
		type: "GET",
		dataType: "json",
		data: {currentQryOrder: qOrder},	
		url: "/xhr/boardorder",
		//error: function(xhr, statusText) { alert("Error: "+statusText); },
		success: function(msg){ 
			/* Don't do anything */
			}
		}
	);
}


function saveErrOrder(qOrder){
// Save the order of realigned error panel queries
	$.ajax({
		type: "GET",
		dataType: "json",
		data: {currentErrOrder: qOrder},	
		url: "/xhr/boardorder",
		//error: function(xhr, statusText) { alert("Error: "+statusText); },
		success: function(msg){ 
			/* Don't do anything */
			}
		}
	);
}

function setupAjax() {
	$(document).ajaxSend(function(event, xhr, settings) {
		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}
		function sameOrigin(url) {
			// url could be relative or scheme relative or absolute
			var host = document.location.host; // host + port
			var protocol = document.location.protocol;
			var sr_origin = '//' + host;
			var origin = protocol + sr_origin;
			// Allow absolute or scheme relative URLs to same origin
			return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
				(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
				// or any other URL that isn't scheme relative or absolute i.e relative.
				!(/^(\/\/|http:|https:).*/.test(url));
		}
		function safeMethod(method) {
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}

		if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
			xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		}
	});
}

function passResetDialog() {
	$(function() {
		var oldpass = $( "#oldpass" ),
			newpass = $( "#newpass" ),
			newpass1 = $( "#newpass1" ),
			allFields = $( [] ).add( oldpass ).add( newpass ).add( newpass1 ),
			tips = $( ".validateTips" );

		function updateTips( t ) {
			tips
				.text( t )
				.addClass( "validation-noimage" );
			setTimeout(function() {
				tips.removeClass( "validation-noimage", 1500 );
			}, 500 );
		}

		function checkLength( o, n, min, max ) {
			if ( o.val().length > max || o.val().length < min ) {
				o.addClass( "ui-state-error" );
				updateTips( "Length of password must be between " +
					min + " and " + max + " characters." );
				return false;
			} else {
				return true;
			}
		}
		
		function checkIfMatch(o, n) {
			if ( o.val() == n.val() ) {
				return true;
			}
			else {
				o.addClass( "ui-state-error" );
				n.addClass( "ui-state-error" );
				updateTips( "Password fields do not match." );
				return false;
			}
		}
		
		$( "#passwordchange-main" ).dialog({
			autoOpen: false,
			height: 250,
			width: 500,
			modal: true,
			closeOnEscape: false,
			draggable: false,
			position: "center",
			buttons: {
				"send": { 
					text: "Change Password",
					class: "buttons defaultbutton",
					click: function() {
						var bValid = true;
						allFields.removeClass( "ui-state-error" );

						bValid = bValid && checkLength( newpass, "newpass", 6, 256 );
						bValid = bValid && checkLength( newpass1, "newpass1", 6, 256 );

						bValid = bValid && checkIfMatch (newpass, newpass1);

						if ( bValid ) {
							$.ajax({
								type: "POST",
								dataType: "json",
								data: {oldpass : oldpass.val(), newpass: newpass.val()},	
								url: "/xhr/changepass/",
								context: $(this),
								success: function(msg){ 
									if (msg.success == true) {
										$( this ).dialog( "close" );		
									}
									else {
										updateTips( msg.errormsg );
									}
								}	
							});
						
							
						}
					}
				},
				"cancel": {
					text: "Cancel",
					class: "buttons",					
					click: function() {
						$( this ).dialog( "close" );
					}
				},
			},
			close: function() {
				allFields.val( "" ).removeClass( "ui-state-error" );
			}
		});

		$( "#changePassword" ).click(function() {
				$( "#passwordchange-main" ).dialog( "open" );
			});
	});
}