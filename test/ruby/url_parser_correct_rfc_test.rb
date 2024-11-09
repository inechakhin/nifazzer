require 'uri'
require 'addressable/uri'
require 'json'

def test_uri_lib(url, part_url)
  parse_url = URI.parse(url)
  if !part_url['scheme'].nil? && (parse_url.scheme.nil? || !part_url['scheme'].casecmp(parse_url.scheme).zero?)
    puts('Problem in scheme:', url, part_url['scheme'], parse_url.scheme)
  end
  if !part_url['userinfo'].nil? && !part_url['userinfo'].casecmp('').zero? && (parse_url.userinfo.nil? || !part_url['userinfo'].casecmp(parse_url.userinfo).zero?)
    puts('Problem in userinfo:', url, part_url['userinfo'], parse_url.userinfo)
  end
  if !part_url['host'].nil? && !part_url['host'].casecmp('').zero? && (parse_url.host.nil? || !part_url['host'].casecmp(parse_url.host).zero?)
    puts('Problem in host:', url, part_url['host'], parse_url.host)
  end
  if (parse_url.port == 80 && !part_url['port'].nil? && !part_url['port'].casecmp('').zero) || (parse_url.port != 80 && part_url['port'].to_i != parse_url.port)
    puts('Problem in port:', url, part_url['port'], parse_url.port)
  end
  if !part_url['path-abempty'].nil? && (parse_url.path.nil? || !part_url['path-abempty'].eql?(parse_url.path))
    puts('Problem in path-abempty:', url, part_url['path-abempty'], parse_url.path)
  end
  if !part_url['query'].nil? && (parse_url.query.nil? || !part_url['query'].eql?(parse_url.query))
    puts('Problem in query:', url, part_url['query'], parse_url.query)
  end
  if !part_url['fragment'].nil? && (parse_url.fragment.nil? || !part_url['fragment'].eql?(parse_url.fragment))
    puts('Problem in fragment:', url, part_url['fragment'], parse_url.fragment)
  end
end

def test_addressable_uri_lib(url, part_url)
  parse_url = Addressable::URI.parse(url)
  if !part_url['scheme'].nil? && (parse_url.scheme.nil? || !part_url['scheme'].casecmp(parse_url.scheme).zero?)
    puts('Problem in scheme:', url, part_url['scheme'], parse_url.scheme)
  end
  userinfo = if parse_url.user.nil? && parse_url.password.nil?
               nil
             elsif !parse_url.user.nil? && parse_url.password.nil?
               parse_url.user
             else
               parse_url.user + ':' + parse_url.password
             end
  if !part_url['userinfo'].nil? && !part_url['userinfo'].casecmp('').zero? && (userinfo.nil? || !part_url['userinfo'].casecmp(userinfo).zero?)
    puts('Problem in userinfo:', url, part_url['userinfo'], userinfo)
  end
  if !part_url['host'].nil? && !part_url['host'].casecmp('').zero? && (parse_url.host.nil? || !part_url['host'].casecmp(parse_url.host).zero?)
    puts('Problem in host:', url, part_url['host'], parse_url.host)
  end
  if !part_url['port'].nil? && !part_url['port'].casecmp('').zero? && (parse_url.port.nil? || part_url['port'].to_i != parse_url.port)
    puts('Problem in port:', url, part_url['port'], parse_url.port)
  end
  if !part_url['path-abempty'].nil? && (parse_url.path.nil? || !part_url['path-abempty'].eql?(parse_url.path))
    puts('Problem in path-abempty:', url, part_url['path-abempty'], parse_url.path)
  end
  if !part_url['query'].nil? && (parse_url.query.nil? || !part_url['query'].eql?(parse_url.query))
    puts('Problem in query:', url, part_url['query'], parse_url.query)
  end
  if !part_url['fragment'].nil? && (parse_url.fragment.nil? || !part_url['fragment'].eql?(parse_url.fragment))
    puts('Problem in fragment:', url, part_url['fragment'], parse_url.fragment)
  end
end

file = File.read('../fuzz/fuzz.json')
arr_url = JSON.parse(file)

puts('Choose option:', '0 - Use uri lib', '1 - Use addressable/uri lib')
num_lib = gets.chomp.to_i

arr_url.each do |t_url|
  url = t_url[0]
  part_url = t_url[1]
  begin
    if num_lib == 0
      test_uri_lib(url, part_url)
    else
      test_addressable_uri_lib(url, part_url)
    end
  rescue Exception
    # puts 'EXCEPTION!'
  end
end
