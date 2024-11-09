require 'uri'
require 'json'

def url_validator1(url)
  if url =~ URI::DEFAULT_PARSER.regexp[:ABS_URI]
    true
  else
    false
  end
end

def url_validator2(url)
  URI.parse(url)
  true
rescue URI::InvalidURIError
  false
end

def url_validator3(url)
  if url =~ URI::DEFAULT_PARSER.make_regexp
    true
  else
    false
  end
end

file = File.read('../fuzz/fuzz.json')
arr_url = JSON.parse(file)
count_full = 0
count_true1 = 0
count_true2 = 0
count_true3 = 0
res_dict = {}
arr_url.each do |t_url|
  url = t_url[0]
  count_full += 1
  count_true1 += 1 if url_validator1(url) == true
  count_true2 += 1 if url_validator2(url) == true
  count_true3 += 1 if url_validator3(url) == true
end
res_dict['URI::DEFAULT_PARSER.make_regexp'] = ((count_true1.to_f / count_full) * 100).to_s + '%'
res_dict['URI parse'] = ((count_true2.to_f / count_full) * 100).to_s + '%'
res_dict['URI::regexp'] = ((count_true3.to_f / count_full) * 100).to_s + '%'
puts res_dict
